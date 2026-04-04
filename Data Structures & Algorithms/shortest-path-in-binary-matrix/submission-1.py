class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        directions =(
            (0, 1), (1, 1), (1, 0), (-1, 1),
            (-1, 0), (-1, -1), (0, -1), (1, -1)
        )

        queue = deque([(0,0)])
        res = 0

        while queue:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()

                if (r, c) == (rows - 1, cols -1):
                    return res + 1

                for dr, dc in directions:
                    r2, c2 = r + dr, c + dc
                    if (
                        0 <= r2 < rows and
                        0 <= c2 < cols and
                        grid[r2][c2] == 0
                    ):
                        queue.append((r2, c2))
                        grid[r][c] = -1
            res += 1
        
        return -1




