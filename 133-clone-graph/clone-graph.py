"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {} #dict to save visited node and respective clone; avoids cycles
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        if node in self.visited:# If the node was already visited before
            return self.visited[node]
        
        clone_node = Node(node.val, []) # Clone the node 
        self.visited[node] = clone_node #and mark it as visited
        
        for neighbor in node.neighbors: # Iterate through the neighbors to clone them and attach to the current node.
            clone_node.neighbors.append(self.cloneGraph(neighbor))
        
        return clone_node