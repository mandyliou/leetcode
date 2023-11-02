# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []  # Return empty list if tree is empty
        
        result = []
        queue = deque([(root, 0)])  # Initialize queue with root node and level 0

        while queue:
            node, level = queue.popleft()  # Dequeue node and its level
            
            # Ensure a sublist exists for the current level
            if len(result) == level:
                result.append([])

            # Append or prepend value based on level
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].insert(0, node.val)

            # Enqueue child nodes with incremented level
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

        return result