# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        cur1, cur2 = l1, l2
        carry = 0
        dummy = cur = ListNode(0, None)

        while (cur1 or cur2) or (carry > 0):
            if cur1 and cur2:
                add = cur1.val + cur2.val + carry
            elif cur1:
                add = cur1.val + carry
            elif cur2:
                add = cur2.val + carry
            else:
                add = carry
            
            carry = add // 10
            
            new = ListNode(add % 10, None)
            cur.next = new
            cur = new
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            
        return dummy.next

        
