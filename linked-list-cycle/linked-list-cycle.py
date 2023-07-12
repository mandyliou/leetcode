# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next: 
            slow = slow.next #moves slow pointer 1 step forward
            fast = fast.next.next #moves fast pointer 2 steps forward
            if slow == fast:#if slow and fast meet, then there's a cycle
                return True
        return False #slow and fast never meet, no cycle 

