class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #create 2D array filled w/ 1's in grid m x n; m = rows, n = columns
        dp = [[1]*n for _ in range(m)] 
        
        #fill the array with sum of above and left cell; starting from (1, 1)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] #i-1 is above; j -1 is left
        return dp[-1][-1] #bottom right corner will have num of unique paths 


# Overall Time: O(m * n)
# Overall Space: O(m * n)