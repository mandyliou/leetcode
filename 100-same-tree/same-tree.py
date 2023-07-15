# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: #both empty, return True
            return True
        if p is None or q is None: #only 1 empty, return False
            return False
        if p.val != q.val: #if values are not both equal
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)