class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c:set() for w in words for c in w}
        indegree = {c:0 for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_length = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""

            for j in range(min_length):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        for k, sett in graph.items():
            for j in sett:
                indegree[j] += 1

        queue = deque()
        for k, value in indegree.items():
            if value == 0:
                queue.append(k)

        visited = set()
        result = ""

        while queue:
            node = queue.popleft()
            visited.add(node)
            result += node

            for nei in graph[node]:
                if nei not in visited:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        queue.append(nei)
        
        if len(result) != len(indegree):
            return ""

        return result
        