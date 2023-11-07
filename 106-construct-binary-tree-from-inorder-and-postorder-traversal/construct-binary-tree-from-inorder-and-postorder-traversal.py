# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # A map to hold the indices of values in inorder for faster lookup
        in_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(low, high):
            if low > high:
                return None
            # The current root is the last element in the current postorder list
            x = TreeNode(postorder.pop())
            # Split the inorder list into left and right subtrees
            mid = in_map[x.val]
            # Recursively build the right subtree
            x.right = build(mid + 1, high)
            # Recursively build the left subtree
            x.left = build(low, mid - 1)
            return x

        return build(0, len(inorder) - 1)