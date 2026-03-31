class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [n for n in nums if n > 0]
        negatives = [n for n in nums if n < 0]
        result = []

        for i in range(len(positives)):
            result.append(positives[i])
            result.append(negatives[i])
        
        print(result)
        return result
