# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        curr = ListNode(0) #will traverse
        dummy = curr #start of linkedlist
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next

            else: #list1.val == list2.val or list1.val > list2.val
                curr.next = list2
                list2 = list2.next
            curr = curr.next #points to most recently added node (end of merged list) 
        curr.next = list1 or list2 #returns first truthy value it encounters

        return dummy.next #returns merged sorted linkedlist, skips initial dummy node
