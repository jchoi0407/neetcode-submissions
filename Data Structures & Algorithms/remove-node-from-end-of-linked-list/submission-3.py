# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        total = 0
        count = head
        while count != None:
            total += 1
            count = count.next
        
        curr = head
        prev = head
        i = 0
        target = total - n
        while i != target:
            prev = curr
            curr = curr.next
            i += 1

        if target == 0:
            curr = curr.next
            prev.next = None
            return curr
        prev.next = curr.next
        curr.next = None
        return head

        
