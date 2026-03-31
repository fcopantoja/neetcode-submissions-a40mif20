class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        for num in nums:
            curr_sum += num
            
            if (curr_sum - k) in prefix:
                res += prefix[curr_sum - k]
            
            prefix[curr_sum] += 1
        
        return res

