# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        # Base case: If the head is None, we've reached end of the list so we just return
        if head is None:
            return
        
        # Recursive call to the next node
        self.printLinkedListInReverse(head.getNext())

        # After the recursive call returns, print the value of the current node
        head.printValue()