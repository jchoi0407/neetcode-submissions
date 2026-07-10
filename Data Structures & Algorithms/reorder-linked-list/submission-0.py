# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # --- find the middle point ---
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if fast != None:
                slow = slow.next

        # --- reverse the 2nd half of the linkedlist
        second = slow.next
        slow.next = None
        prev = None
        while second != None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the 1st half & 2nd half by alternating
        first = head
        second = prev
        while second != None:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            first = temp1
            second.next = first
            second = temp2
        
        
                
            
            



 


