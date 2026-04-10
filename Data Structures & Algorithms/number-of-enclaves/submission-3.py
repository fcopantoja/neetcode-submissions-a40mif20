class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        lands = 0
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    lands += 1
                if (row == 0 or row == rows -1 or col == 0 or col == cols - 1) and grid[row][col] == 1:
                    queue.append((row, col))
                    grid[row][col] = 2
                    lands -= 1

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]       
        while queue:
            for _ in range(len(queue)):
                r, c  = queue.popleft()
                visited.add((r, c))

                for dr, dc in directions:
                    r2, c2 = r + dr, c + dc

                    if (
                        r2 in range(rows) and
                        c2 in range(cols) and
                        (r2, c2) not in visited and
                        grid[r2][c2] == 1
                    ):
                        grid[r2][c2] = 2
                        lands -= 1
                        queue.append((r2, c2))
                        visited.add((r2, c2))
        
        return lands
