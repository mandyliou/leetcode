# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if empty or single-node, no need to sort; makes it more efficient
        if not head or not head.next:
            return head
            
        dummy = ListNode(0) #new starting point
        dummy.next = head
        prev = dummy
        curr = head
        while curr and curr.next:
            if curr.val <= curr.next.val: #curr node in right position
                curr = curr.next #moves onto next node 
            else: #if next node is bigger, need to move curr.next to correct position
                temp = curr.next
                curr.next = curr.next.next #unlink curr.next
                x = dummy
                y = dummy.next
                while y.val < temp.val:
                    x = y
                    y = y.next
                x.next = temp
                temp.next = y
        return dummy.next

            
            