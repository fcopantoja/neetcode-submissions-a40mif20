class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        stack = []

        for idx, num in enumerate(nums2):
            while stack and stack[-1] < num:
                n = stack.pop()
                hmap[n] = num
            stack.append(num)
        
        result = []
        for num in nums1:
            result.append(hmap.get(num, -1))
        return result

            


            



