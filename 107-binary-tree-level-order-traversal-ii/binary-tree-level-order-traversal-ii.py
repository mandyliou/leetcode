# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # Return an empty list if the tree is empty
            return []
        
        queue = deque([root])  # Queue for BFS, initialized with the root node
        result = deque()  # Use deque for efficient append operations at the beginning

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()  # Remove the next node from the queue
                level.append(node.val)  # Add node's value to current lvl list

                # Add the node's children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.appendleft(level)  # Add the lvl at the beginning of the result

        return list(result)  # Convert deque to list before returning        