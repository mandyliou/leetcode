# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        # Dummy node to start the new list
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize current node to dummy
        curr = dummy
        
        while curr:
            for _ in range(m): # Keep the first 'm' nodes
                if curr:
                    curr = curr.next
            
            # If we reached the end, break
            if not curr:
                break
            
            # Delete the next 'n' nodes
            for _ in range(n):
                if curr.next:
                    curr.next = curr.next.next
            
        return dummy.next