class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        from collections import deque
        import sys
        n = len(graph)
        
        # Step 1: BFS to find shortest paths between all pairs of nodes
        dist = [[sys.maxsize] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
            queue = deque([i])
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if dist[i][neighbor] == sys.maxsize:  # Not visited
                        dist[i][neighbor] = dist[i][node] + 1
                        queue.append(neighbor)
        
        # Step 2: Dynamic Programming with Bitmasking
        dp = [[sys.maxsize] * n for _ in range(1 << n)]
        
        for i in range(n):
            dp[1 << i][i] = 0  # Starting at each node
        
        for mask in range(1 << n):
            for u in range(n):
                if dp[mask][u] == sys.maxsize:
                    continue
                for v in range(n):
                    if mask & (1 << v) == 0:  # v is not visited
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
        
        # Step 3: Find the minimum path covering all nodes
        final_mask = (1 << n) - 1
        min_length = sys.maxsize
        
        for i in range(n):
            min_length = min(min_length, dp[final_mask][i])
        
        return min_length