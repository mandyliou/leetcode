# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
         # Helper function to create BST from sorted array
        def createBST(left, right):
            if left > right: #when sub-array is empty
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = createBST(left, mid - 1) #recursively construct left subtrees
            root.right = createBST(mid + 1, right)

            return root

        return createBST(0, len(nums) - 1) #Start BST creation from the whole array