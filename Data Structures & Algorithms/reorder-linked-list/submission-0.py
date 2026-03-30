# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing second half
        
        curr = slow.next
        prev = slow.next = None
        while curr:
            
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        

        curr1, curr2 = head, prev

        while curr1 and curr2:
            temp1 = curr1.next  
            temp2 = curr2.next 
            curr1.next = curr2
            curr2.next = temp1
            curr1 = temp1
            curr2 = temp2
        
