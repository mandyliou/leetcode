# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None: #base case: empty tree has height 0
                return 0
            else:
                left_height = dfs(root.left) #recursively compute height of both sides
                right_height = dfs(root.right)
                #if left or right tree is not balanced OR height diff is greater than 1, then return -1 to indicate unbalanced 
                if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                    return -1 
                else: #if tree is balanced, return max height
                    return max(left_height, right_height) + 1
        return dfs(root) != -1 #tree is balanced if it doesn't return -1

        