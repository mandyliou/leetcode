# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head #starts at 1
        while temp and temp.next: #every iteration, head moves 1, tail moves 2
            head = head.next 
            temp = temp.next.next
        return head

#initialize: h=1, t=1
#iteration1: h=2, t=3
#iteration2: h=3, t=5
#iteration3: h=4, t=7
#iteration4: h=5, t=none
