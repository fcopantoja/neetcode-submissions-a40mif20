# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            
            dummy.next = ListNode(val=val)
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next
































class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        curr = head
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            
            curr.next = ListNode(val % 10)
            carry = val // 10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)

        return head.next



