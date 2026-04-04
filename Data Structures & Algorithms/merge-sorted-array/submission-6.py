class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums1) - 1
        l = length - n
        r = length

        while l >= 0:
            nums1[l], nums1[r] = nums1[r], nums1[l]
            l -= 1
            r -= 1
        
        for i in range(n):
            nums1[i] = nums2[i]
        
        nums1.sort()
        
        return nums1


        