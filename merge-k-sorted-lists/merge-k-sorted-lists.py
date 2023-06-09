# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0: #if list is empty, return None
            return None
        while len(lists) > 1: #when theres more than 1 list left, keep merging
            merged = []
            for i in range(0, len(lists), 2): #iterate in pairs
                l1 = lists[i] #first list for merging
				#if there's another list, set it as l2; 
                if (i + 1) < len(lists):
                    l2 = lists[i+1]
                else: #no other list, set l2 to none
                    l2 = None
                merged.append(self.mergeLists(l1, l2)) #merge l1+l2, append result to merged
            lists = merged #replace 'lists' w 'merged' for next while iteration
        return lists[0] #returns single list left after all merges

    def mergeLists(self, l1, l2):
        dummy = ListNode(0) #making a starting point
        tail = dummy #create tail pointer pointing to dummy node
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next #moves tail pointer to appended node above
		
        #leftover nodes:
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next