class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sett = set(range(1, len(nums) + 2))
        for num in nums:
            if num in sett:
                sett.remove(num)
        print(sett)
        if sett:
            return list(sett)[0]
        return 1