class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        dp = {}

        def backtracking(i, t):
            if (i, t) in dp:
                return dp[(i, t)]
            if target == t:
                return True
            if i == len(nums):
                return False

            a = backtracking(i + 1, t + nums[i])
            b = backtracking(i + 1, t)
            dp[(i, t)] = a or b
            return dp[(i, t)]

        return backtracking(0, 0)
        