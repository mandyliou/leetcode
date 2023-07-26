# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) 
        dummy.next = head 
        prev = dummy #initialize 2 pointers: prev & curr
        curr = head
        node_sum = 0
        
        while curr:
            if curr.val != 0: #if current value is NOT 0, add it to sum
                node_sum += curr.val 
                curr = curr.next #move to next node
            else: #if curr value is 0, 
                if node_sum: #if there's nodes to merge, 
                    new_node = ListNode(node_sum) #create new node with node's sum
                    prev.next = new_node #link new node
                    new_node.next = curr.next #skip the 0 node and link new node to the node after the zero node
                    prev = new_node #move previous node to the new node
                else: #if no node to merge, 
                    prev.next = curr.next #Skip the 0 node (node_sum is 0)
                curr = curr.next #move to next node
                node_sum = 0 #reset node sum back to 0

        return dummy.next #return modified list, exclude dummy node
