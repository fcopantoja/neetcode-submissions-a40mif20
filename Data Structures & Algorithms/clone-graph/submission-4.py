"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraphBFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        queue = deque([node])
        start = node
        visited = set()
        visited.add(node)
        oldNewMapping = {}

        while queue:
            current = queue.popleft()
            oldNewMapping[current] = Node(val=current.val)

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        for old_node, new_node in oldNewMapping.items():
            for nei in old_node.neighbors:
                new_node.neighbors.append(oldNewMapping[nei])
        
        return oldNewMapping[start]


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_mapping = {}
        visited = set()
        head = node

        def dfs(node):
            if not node:
                return
            
            new_node = Node(val=node.val)
            old_mapping[node] = new_node

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        dfs(node)

        for old, new in old_mapping.items():
            for nei in old.neighbors:
                new.neighbors.append(old_mapping[nei])
        
        return old_mapping[head]

        
        
        