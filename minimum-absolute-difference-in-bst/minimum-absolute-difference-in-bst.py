# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(r):
            if r:
                return inorder(r.left) + [r.val] + inorder(r.right)
            else: #r(node) is none (leaf node) -> return empty list
                return []
        nums = inorder(root) #call inorder on the root of tree, will return list of all nodes in ascending order

        min_diff = float('inf') #set min_diff to infinity
        for x,y in zip(nums, nums[1:]): #loop over neighboring values
            diff = abs(x-y) #calculate abs diff b/w each pair
            if diff < min_diff: #if diff is smaller than min_diff, update min_diff
                min_diff = diff
        return min_diff #after the loop, min_diff is abs smallest diff b/w 2 nodes