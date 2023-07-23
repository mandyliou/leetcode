# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(orig, clone):
            if orig is None: # If the current node in original is None (leaf node), return None
                return None
            if orig == target: #If the current node in original is the target, return the corresponding node in cloned
                return clone
            # Continue the DFS on the left and right subtrees.
            # If the target is found in the left subtree, the result will not be None, and will be returned.
            # If the target is not found in the left subtree, the search continues in the right subtree.
            return dfs(orig.left, clone.left) or dfs(orig.right, clone.right)

        return dfs(original, cloned) # Call the DFS function on the root of the original and cloned trees.
