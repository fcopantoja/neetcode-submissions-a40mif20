from _heapq import heapify
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSumNaive(self, head: Optional[ListNode]) -> int:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        l = 0
        r = len(nums) - 1
        res = float("-inf")

        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1

        
        return res

    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse after middle node
        curr, previous = slow, None
        while curr:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node
        
        curr1, curr2 = head, previous
        res = 0
        while curr1 and curr2:
            res = max(res, curr1.val + curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next
        
        return res
