class Solution:
    def findRedundantConnectionTopological(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {x:[] for x in range(1, n + 1)}
        indegree = [0] * (n + 1)


        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                queue.append(i)

        while queue:
            node = queue.popleft()
            indegree[node] -= 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)


        for edge in reversed(edges):
            if indegree[edge[0]] > 0 and indegree[edge[1]] > 0:
                return edge
            
        return []
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n1):
            print(parent)
            if parent[n1] != n1:
                parent[n1] = find(parent[n1])
            
            return parent[n1]
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        

        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        
        return []


