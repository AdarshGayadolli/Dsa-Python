from collections import deque
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        max_depth = 0
        queue = deque([(1, 0)])
        visited = [False] * (n + 1)
        visited[1] = True

        while queue:
            curr, depth = queue.popleft()
            max_depth = max(max_depth, depth)

            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, depth + 1))

        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)
