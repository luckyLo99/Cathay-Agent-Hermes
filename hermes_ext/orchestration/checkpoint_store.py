from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

from hermes_ext.orchestration.contracts import (
    CheckpointKind,
    ShadowCheckpoint,
    ShadowStepName,
)


class CheckpointStore:
    """
    Isolated SQLite checkpoint store.

    It never touches Hermes state DB.
    """

    SCHEMA_VERSION = 1

    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
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
                CREATE TABLE IF NOT EXISTS shadow_checkpoint_meta (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                INSERT OR REPLACE INTO shadow_checkpoint_meta(key, value)
                VALUES ('schema_version', ?)
                """,
                (str(self.SCHEMA_VERSION),),
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS shadow_checkpoints (
                    checkpoint_id TEXT PRIMARY KEY,
                    run_id TEXT NOT NULL,
                    session_id TEXT NOT NULL,
                    step_name TEXT NOT NULL,
                    kind TEXT NOT NULL,
                    sequence INTEGER NOT NULL,
                    state_json TEXT NOT NULL,
                    state_hash TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    error TEXT
                )
                """
            )
            conn.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_shadow_checkpoints_run_sequence
                ON shadow_checkpoints(run_id, sequence)
                """
            )
            conn.commit()

    def write(self, checkpoint: ShadowCheckpoint) -> ShadowCheckpoint:
        checkpoint = checkpoint.with_hash()

        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO shadow_checkpoints(
                    checkpoint_id, run_id, session_id, step_name, kind,
                    sequence, state_json, state_hash, created_at, error
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    checkpoint.checkpoint_id,
                    checkpoint.run_id,
                    checkpoint.session_id,
                    checkpoint.step_name.value,
                    checkpoint.kind.value,
                    checkpoint.sequence,
                    json.dumps(checkpoint.state, ensure_ascii=False, sort_keys=True),
                    checkpoint.state_hash,
                    checkpoint.created_at.isoformat(),
                    checkpoint.error,
                ),
            )
            conn.commit()

        return checkpoint

    def get(self, checkpoint_id: str) -> ShadowCheckpoint | None:
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT * FROM shadow_checkpoints
                WHERE checkpoint_id = ?
                """,
                (checkpoint_id,),
            ).fetchone()

        if row is None:
            return None

        return self._row_to_checkpoint(row)

    def list_run(self, run_id: str) -> list[ShadowCheckpoint]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT * FROM shadow_checkpoints
                WHERE run_id = ?
                ORDER BY sequence ASC
                """,
                (run_id,),
            ).fetchall()

        return [self._row_to_checkpoint(row) for row in rows]

    def latest_for_run(self, run_id: str) -> ShadowCheckpoint | None:
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT * FROM shadow_checkpoints
                WHERE run_id = ?
                ORDER BY sequence DESC
                LIMIT 1
                """,
                (run_id,),
            ).fetchone()

        if row is None:
            return None

        return self._row_to_checkpoint(row)

    def count(self, run_id: str | None = None) -> int:
        with self._connect() as conn:
            if run_id is None:
                row = conn.execute("SELECT COUNT(*) AS count FROM shadow_checkpoints").fetchone()
            else:
                row = conn.execute(
                    "SELECT COUNT(*) AS count FROM shadow_checkpoints WHERE run_id = ?",
                    (run_id,),
                ).fetchone()
        return int(row["count"])

    def assert_shadow_tables_only(self) -> bool:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT name FROM sqlite_master
                WHERE type IN ('table', 'index')
                """
            ).fetchall()

        names = [str(row["name"]) for row in rows]
        allowed_prefixes = ("shadow_", "idx_shadow_", "sqlite_")
        return all(name.startswith(allowed_prefixes) for name in names)

    def _row_to_checkpoint(self, row: sqlite3.Row) -> ShadowCheckpoint:
        return ShadowCheckpoint(
            checkpoint_id=str(row["checkpoint_id"]),
            run_id=str(row["run_id"]),
            session_id=str(row["session_id"]),
            step_name=ShadowStepName(str(row["step_name"])),
            kind=CheckpointKind(str(row["kind"])),
            sequence=int(row["sequence"]),
            state=json.loads(str(row["state_json"])),
            state_hash=str(row["state_hash"]),
            created_at=datetime.fromisoformat(str(row["created_at"])),
            error=row["error"],
        )