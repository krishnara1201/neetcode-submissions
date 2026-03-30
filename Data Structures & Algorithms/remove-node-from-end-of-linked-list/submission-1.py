# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        forward = head
        while forward and n > 0:
            forward = forward.next
            n -= 1
        
        dummy = ListNode(0, head)
        current = dummy
        while forward:
            forward = forward.next
            current = current.next

        temp = current.next.next
        current.next = None
        current.next = temp

        return dummy.next