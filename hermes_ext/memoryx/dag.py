from __future__ import annotations

from collections import defaultdict, deque

from pydantic import BaseModel, ConfigDict, Field

from hermes_ext.memoryx.contracts import ShadowMemoryEdge, ShadowMemoryNode


class ShadowMemoryDAG(BaseModel):
    """
    In-memory DAG validator.

    The SQLite provider stores edges. This class validates the acyclic graph shape.
    """

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    nodes: dict[str, ShadowMemoryNode] = Field(default_factory=dict)
    edges: list[ShadowMemoryEdge] = Field(default_factory=list)

    def add_node(self, node: ShadowMemoryNode) -> "ShadowMemoryDAG":
        nodes = dict(self.nodes)
        nodes[node.node_id] = node
        return self.model_copy(update={"nodes": nodes})

    def add_edge(self, edge: ShadowMemoryEdge) -> "ShadowMemoryDAG":
        if edge.source_node_id not in self.nodes:
            raise ValueError(f"source node missing: {edge.source_node_id}")
        if edge.target_node_id not in self.nodes:
            raise ValueError(f"target node missing: {edge.target_node_id}")

        candidate = self.model_copy(update={"edges": [*self.edges, edge]})
        if candidate.has_cycle():
            raise ValueError("edge would create cycle")
        return candidate

    def has_cycle(self) -> bool:
        graph: dict[str, list[str]] = defaultdict(list)
        indegree: dict[str, int] = {node_id: 0 for node_id in self.nodes}

        for edge in self.edges:
            graph[edge.source_node_id].append(edge.target_node_id)
            indegree[edge.target_node_id] = indegree.get(edge.target_node_id, 0) + 1

        queue = deque([node_id for node_id, degree in indegree.items() if degree == 0])
        visited = 0

        while queue:
            node_id = queue.popleft()
            visited += 1
            for target in graph[node_id]:
                indegree[target] -= 1
                if indegree[target] == 0:
                    queue.append(target)

        return visited != len(indegree)

    def parents_of(self, node_id: str) -> list[str]:
        return [edge.source_node_id for edge in self.edges if edge.target_node_id == node_id]

    def children_of(self, node_id: str) -> list[str]:
        return [edge.target_node_id for edge in self.edges if edge.source_node_id == node_id]