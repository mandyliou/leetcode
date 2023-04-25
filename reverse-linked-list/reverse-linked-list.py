# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case 
        if not head or not head.next:
            return head
        #if there's a head, obtain new head of the reversed list from the recursive call
        newHead = self.reverseList(head.next)
        #reverses the link between head and its next node, will make next node point to "head"
        head.next.next = head
        #then sets head.next to None to break the link between head and its original next node
        head.next = None 
        return newHead
