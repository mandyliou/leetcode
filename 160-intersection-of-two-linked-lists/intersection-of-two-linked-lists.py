# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: #if theres None of headA or headB, intersection is NOT possible -> hence None
            return None

        # Initialize pointers ptrA and ptrB 
        ptrA = headA
        ptrB = headB

        while ptrA != ptrB: # Traverse both lists
            # When ptrA reaches the end of list A, redirect it to the head of list 
            ptrA = headB if ptrA is None else ptrA.next
            
            # When ptrB reaches the end of list B, redirect it to the head of list 
            ptrB = headA if ptrB is None else ptrB.next

        # If there's an intersection, ptrA and ptrB will meet at intersection point
        # If there's no intersection, they will meet at the end (None)
        return ptrA