# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: #if list is empty or only has 1 node, can't have cycle
            return False
        slow = head #starts at 1st node
        fast = head.next #starts at 2nd node

        while slow != fast: #while slow and fast do NOT meet...
            #if fast pointer reached end of list, there's no cycle
            if fast is None or fast.next is None: 
                return False
            slow = slow.next #moves slow pointer 1 step forward
            fast = fast.next.next #moves fast pointer 2 steps forward
        return True #if slow and fast meet, then there's a cycle

