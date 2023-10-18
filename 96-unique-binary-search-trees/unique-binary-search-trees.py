class Solution:
    def numTrees(self, n: int) -> int:
         # DP array to store the number of unique BSTs
        G = [0] * (n + 1)
        
        # Base cases
        G[0], G[1] = 1, 1
        
        # Fill in the DP array
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                G[nodes] += G[root - 1] * G[nodes - root]
                
        return G[n]