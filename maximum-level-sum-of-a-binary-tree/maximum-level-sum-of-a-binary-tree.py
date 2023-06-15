# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root) -> int:
        q = collections.deque() #BFS uses queue, creates a queue "FIFO"
        q.append(root) #add root to queue

        max_sum = float('-inf') #sets max_sum to negative infinity
        lvl = 1 #starts at root
        maxlvl = 0

        while q: #q isn't empty
            curr_sum = 0 #initialize curr lvl sum as 0
            for _ in range(len(q)):
                node = q.popleft() #pop node from left of queue
                curr_sum += node.val #add the node's val to current level
                #add children of curr node to queue if they exist
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if curr_sum > max_sum: #after summing all val at curr level, compare it to max_sum
                max_sum = curr_sum 
                maxlvl = lvl
            lvl += 1 #increase lvl by 1 as we move to next level in next iteration
        return maxlvl #return the level with the max sum




