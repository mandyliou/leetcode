# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
         # Initialize variables to keep track of the incorrectly placed nodes
        first_node, second_node, prev_node = None, None, None
        current_node = root
        stack = []
        
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            
            # Process the node at the top of the stack
            current_node = stack.pop()
            
            # If we found a violation of BST property
            if prev_node and prev_node.val > current_node.val:
                if not first_node:
                    first_node = prev_node  # First wrongly placed node
                second_node = current_node  # Second wrongly placed node
                
            prev_node = current_node
            current_node = current_node.right
        
        # Swap the values of the two wrongly placed nodes
        first_node.val, second_node.val = second_node.val, first_node.val