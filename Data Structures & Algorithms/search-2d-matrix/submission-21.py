class Solution:
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1
        middle = (bottom + top) // 2

        while bottom <= top:
            middle = (bottom + top) // 2
            if matrix[middle][0] == target or matrix[middle][-1] == target:
                return True
            if matrix[middle][0] < target and matrix[middle][-1] > target:
                break
            if matrix[middle][0] < target:
                bottom = middle + 1
            else:
                top = middle - 1

        return self.binary_search(matrix[middle], target)
    
    def binary_search(self, arr: List[int], target: int):
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == target:
                return True

            if arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        top = 0
        bottom = rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            print(mid)
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                break
            if target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1
        
        row = mid
        print('row is', row)
        l = 0
        r = cols - 1
        while l <= r:
            middle = (l + r) // 2
            if matrix[row][middle] == target:
                return True
            if target > matrix[row][middle]:
                l = middle + 1
            else:
                r = middle - 1
        
        return False
        
        

