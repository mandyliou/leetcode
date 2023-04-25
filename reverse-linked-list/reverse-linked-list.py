# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head #current was originally head
        while curr:
            nxt = curr.next
            curr.next = prev #set to previous
            prev = curr
            curr = nxt
        return prev
