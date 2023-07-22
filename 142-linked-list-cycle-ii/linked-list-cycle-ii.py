# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        if head is None:
            return None

        # Phase 1: Detecting cycle using Floyd's Cycle Detection Algorithm
        slow = fast = head #initialize slow and fast pointer
        while fast is not None and fast.next is not None:
            slow = slow.next #slow moves 1 step
            fast = fast.next.next #fast moves 2 steps
            if slow == fast: #if slow and fast meets, there's a cycle
                break

        # check: if fast reached the end, no cycle was detected
        if fast is None or fast.next is None: 
            return None

        # Phase 2: Finding start node of the cycle; slow and fast pointers move 1 step at a time
        slow = head #initialize slow back to head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow #the point where slow and fast meet is the start of the cycle 
