# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #direction of pointers in each node to point to prev node
        #start with changing head pointer to point it to null
        prev = None
        curr = head
        while curr:
            new_head = curr.next #temp stores next node
            curr.next = prev #reverse pointers
            prev = curr #update prev
            curr = new_head #update curr
        return prev