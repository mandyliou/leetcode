# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head: #traverse the list
            # Shift result to left (multiply by 2) & add current node's value
            result = result * 2 + head.val
            head = head.next #move to next head
        return result