import math
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        counts = defaultdict(int)
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                counts[grid[row][col]] += 1
        
        a = b = 0
        print(counts)
        for num in range(n ** 2 + 1):
            if counts[num] == 2:
                a = num
            elif counts[num] == 0:
                b = num

        return [a, b]


        



                
        