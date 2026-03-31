class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []

        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        i = 0

        while 2 * i + 1 < len(nums):
            nums[2 * i] = positives[i]
            nums[2 * i + 1] = negatives[i]
            i += 1
        
        return nums

    def rearrangeArrayExtraSpace(self, nums: List[int]) -> List[int]:
        positives = [n for n in nums if n > 0]
        negatives = [n for n in nums if n < 0]
        result = []
        
        for i in range(len(nums)):
            result.append(positives[i])
            result.append(negatives[i])
        
        return result

