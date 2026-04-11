class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        product = 1
        res = 0

        while r < len(nums):
            product = product * nums[r]

            while l <= r and product >= k:
                product = product // nums[l]
                l += 1
            
            print(r, l)
            res += (r - l + 1)
            r += 1
        
        return res
        