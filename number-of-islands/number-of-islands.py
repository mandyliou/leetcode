#want island(1); not water(0)
class Solution:
    def numIslands(self, grid) -> int:
        if not grid: #check if grid is empty
            return 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            #if indices are out of bounds, or current cell is water -> return
            if (r < 0 or c < 0) or (r >= rows or c >= cols) or (grid[r][c] == "0"):
                return
            #mark current cell as 0 if it's been visited
            grid[r][c] = "0"
            dfs(r + 1, c) #down
            dfs(r - 1, c) #up
            dfs(r, c + 1) #right
            dfs(r, c - 1) #left
        
        island = 0 #initial count of island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": #if it's island(1)
                    dfs(r, c) #perform dfs to find the island
                    island += 1 #increase count of islands by 1
        return island #return total count of island


            

