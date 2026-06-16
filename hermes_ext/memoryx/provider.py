from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

from hermes_ext.memoryx.contracts import (
    MemoryNodeKind,
    MemoryNodeStatus,
    MemoryPIILevel,
    ShadowMemoryEdge,
    ShadowMemoryNode,
    ShadowMemoryQuery,
    ShadowMemoryRecallResult,
    ShadowMemoryWriteRequest,
)
from hermes_ext.memoryx.pii import ShadowPIIFilter


class ShadowMemoryProvider:
    """
    Isolated SQLite-backed shadow memory provider.

    It never touches Hermes native memory tables.
    """

    SCHEMA_VERSION = 1

    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.pii_filter = ShadowPIIFilter()
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS shadow_schema_meta (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                INSERT OR REPLACE INTO shadow_schema_meta(key, value)
                VALUES ('schema_version', ?)
                """,
                (str(self.SCHEMA_VERSION),),
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS shadow_memory_nodes (
                    node_id TEXT PRIMARY KEY,
                    trace_id TEXT NOT NULL,
                    session_id TEXT NOT NULL,
                    turn_id TEXT NOT NULL,
                    kind TEXT NOT NULL,
                    status TEXT NOT NULL,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    content_hash TEXT NOT NULL,
                    source TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    pii_level TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    metadata_json TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS shadow_memory_edges (
                    edge_id TEXT PRIMARY KEY,
                    source_node_id TEXT NOT NULL,
                    target_node_id TEXT NOT NULL,
                    edge_type TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    reason TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY(source_node_id) REFERENCES shadow_memory_nodes(node_id),
                    FOREIGN KEY(target_node_id) REFERENCES shadow_memory_nodes(node_id)
                )
                """
            )
            conn.execute(
                """
                CREATE VIRTUAL TABLE IF NOT EXISTS shadow_memory_fts
                USING fts5(node_id UNINDEXED, title, content)
                """
            )
            conn.commit()

    def write(self, request: ShadowMemoryWriteRequest) -> ShadowMemoryNode:
        node = request.node.with_hash()

        pii = self.pii_filter.detect(node.content)
        if pii.level != MemoryPIILevel.NONE:
            node = node.model_copy(
                update={
                    "pii_level": pii.level,
                    "metadata": {
                        **node.metadata,
                        "pii_reasons": pii.reasons,
                    },
                }
            )

        if node.pii_level == MemoryPIILevel.HIGH:
            node = node.model_copy(update={"status": MemoryNodeStatus.QUARANTINED})

        if node.status == MemoryNodeStatus.QUARANTINED and not request.allow_quarantine:
            raise ValueError("quarantined node rejected by request")

        node = node.with_hash()

        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO shadow_memory_nodes(
                    node_id, trace_id, session_id, turn_id, kind, status,
                    title, content, content_hash, source, confidence,
                    pii_level, created_at, metadata_json
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    node.node_id,
                    node.trace_id,
                    node.session_id,
                    node.turn_id,
                    node.kind.value,
                    node.status.value,
                    node.title,
                    node.content,
                    node.content_hash,
                    node.source,
                    node.confidence,
                    node.pii_level.value,
                    node.created_at.isoformat(),
                    json.dumps(node.metadata, ensure_ascii=False, sort_keys=True),
                ),
            )
            conn.execute(
                """
                INSERT OR REPLACE INTO shadow_memory_fts(node_id, title, content)
                VALUES (?, ?, ?)
                """,
                (node.node_id, node.title, node.content),
            )

            for edge in request.edges:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO shadow_memory_edges(
                        edge_id, source_node_id, target_node_id,
                        edge_type, confidence, reason, created_at
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        edge.edge_id,
                        edge.source_node_id,
                        edge.target_node_id,
                        edge.edge_type.value,
                        edge.confidence,
                        edge.reason,
                        edge.created_at.isoformat(),
                    ),
                )

            conn.commit()

        return node

    def get(self, node_id: str) -> ShadowMemoryNode | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM shadow_memory_nodes WHERE node_id = ?",
                (node_id,),
            ).fetchone()

        if row is None:
            return None

        return self._row_to_node(row)

    def recall(self, query: ShadowMemoryQuery) -> list[ShadowMemoryRecallResult]:
        where = []
        params: list[Any] = []

        if not query.include_quarantined:
            where.append("n.status != ?")
            params.append(MemoryNodeStatus.QUARANTINED.value)

        if query.kinds:
            placeholders = ",".join("?" for _ in query.kinds)
            where.append(f"n.kind IN ({placeholders})")
            params.extend([kind.value for kind in query.kinds])

        where_sql = " AND ".join(where)
        if where_sql:
            where_sql = "WHERE " + where_sql

        like_query = f"%{query.query}%"

        with self._connect() as conn:
            try:
                rows = conn.execute(
                    f"""
                    SELECT n.*, bm25(shadow_memory_fts) AS rank_score
                    FROM shadow_memory_fts
                    JOIN shadow_memory_nodes n ON n.node_id = shadow_memory_fts.node_id
                    {where_sql}
                    AND shadow_memory_fts MATCH ?
                    ORDER BY rank_score ASC
                    LIMIT ?
                    """,
                    [*params, query.query, query.limit],
                ).fetchall()
                matched_by = "fts5"
            except sqlite3.OperationalError:
                rows = conn.execute(
                    f"""
                    SELECT n.*, 1.0 AS rank_score
                    FROM shadow_memory_nodes n
                    {where_sql}
                    {'AND' if where_sql else 'WHERE'} (n.title LIKE ? OR n.content LIKE ?)
                    LIMIT ?
                    """,
                    [*params, like_query, like_query, query.limit],
                ).fetchall()
                matched_by = "like"

        results: list[ShadowMemoryRecallResult] = []
        for row in rows:
            rank = float(row["rank_score"])
            score = 1.0 / (1.0 + abs(rank))
            results.append(
                ShadowMemoryRecallResult(
                    node=self._row_to_node(row),
                    score=score,
                    matched_by=matched_by,
                )
            )

        return results

    def list_nodes(self, *, limit: int = 100) -> list[ShadowMemoryNode]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT * FROM shadow_memory_nodes
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

        return [self._row_to_node(row) for row in rows]

    def count_nodes(self) -> int:
        with self._connect() as conn:
            row = conn.execute("SELECT COUNT(*) AS count FROM shadow_memory_nodes").fetchone()
        return int(row["count"])

    def _row_to_node(self, row: sqlite3.Row) -> ShadowMemoryNode:
        return ShadowMemoryNode(
            node_id=str(row["node_id"]),
            trace_id=str(row["trace_id"]),
            session_id=str(row["session_id"]),
            turn_id=str(row["turn_id"]),
            kind=MemoryNodeKind(str(row["kind"])),
            status=MemoryNodeStatus(str(row["status"])),
            title=str(row["title"]),
            content=str(row["content"]),
            content_hash=str(row["content_hash"]),
            source=str(row["source"]),
            confidence=float(row["confidence"]),
            pii_level=MemoryPIILevel(str(row["pii_level"])),
            created_at=datetime.fromisoformat(str(row["created_at"])),
            metadata=json.loads(str(row["metadata_json"])),
        )