# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        new = []
        current = head

        while current:
            new.append(current)
            current = current.next
        mid_index = len(new) // 2
        
        return new[mid_index]
