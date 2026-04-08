class Solution:
    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            v1 = dp[i - 1]
            v2 = nums[i] + dp[i - 2]
            dp[i] = max(v1, v2)
            
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0

            v1 = dfs(i + 1)
            v2 = nums[i] + dfs(i + 2)
            memo[i] = max(v1, v2)
            return memo[i]
        
        return dfs(0)
