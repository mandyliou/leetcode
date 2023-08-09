# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')): #helper function to validate isValidBST
            if not node: #base case: if current node is none/leaf node, return True
                return True
            if node.val <= low or node.val >= high: #if current node's out of allowable range 
                return False
            #for left child, value should be less than the current node's value by updating the 'high' bound
            #for the right child, value should be greater than current node's value by updating the 'low' bound
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root) #start the validation process from the root 

#time: O(n) -> n is num of nodes in tree; will visit each node once
#space: O(h) -> h is height of tree; skewed tree (worst case) h=n; balanced(best case) h = log(n)