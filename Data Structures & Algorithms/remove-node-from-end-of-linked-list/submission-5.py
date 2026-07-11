# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ans = ListNode()
        ans.next = head
        left = ans
        right = head
        while n > 0:
            right = right.next
            n -= 1
        
        while right != None:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return ans.next
        


        