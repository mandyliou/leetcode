# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            # If both nodes are None, they are symmetric
            if not left and not right:
                return True
            # If one of the nodes is None, they are not symmetric
            if not left or not right:
                return False
            # Compare values of the current nodes and their subtrees
            return (left.val == right.val) and \
                   isMirror(left.left, right.right) and \
                   isMirror(left.right, right.left)
        
        # Check if the tree is symmetric starting from the root
        return isMirror(root, root)