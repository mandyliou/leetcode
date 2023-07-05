# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #main fxn, checks if binary tree is balanced or not
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        return (self.Height(root) >= 0) #balanced tree is positive or 0
    
    #helper fxn calculates height of binary tree
    def Height(self, root) -> bool:
        if root is None: #if tree's empty, return 0 -> thus balanced
            return 0 
        #or calculate height of l/r subtrees
        leftheight = self.Height(root.left)
        rightheight = self.Height(root.right)

        #if height of either subtree is neg, OR diff b/w height > 1 -> tree is not balanced -> return -1
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        #if tree is balanced, return the height of the max plus 1
        return max(leftheight, rightheight) + 1




        
        