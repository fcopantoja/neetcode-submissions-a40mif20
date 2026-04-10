from _heapq import heapify
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeLists(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(-1)
        head = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        
        return head.next
            


    """def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        
        for lst in lists:
            result = self.mergeLists(result, lst)

        return result"""

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for arr in lists:
            curr = arr
            while curr:
                min_heap.append(curr.val)
                curr = curr.next
        
        heapq.heapify(min_heap)
        dummy = ListNode(-1)
        curr = dummy
        while min_heap:
            curr.next = ListNode(heapq.heappop(min_heap))
            curr = curr.next
        
        return dummy.next

        