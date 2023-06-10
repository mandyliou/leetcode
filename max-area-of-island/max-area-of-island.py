class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if (min(r, c) < 0) or (r >= rows or c >= cols) or (grid[r][c] == 0):
                return 0
            grid[r][c] = 0 #
            d = dfs(r+1, c) 
            u = dfs(r-1, c)
            right = dfs(r, c+1)
            l = dfs(r, c-1)
            return d + u + right + l + 1 #include current cell, which is 1

        area = 0
        for r in range(rows):
            for c in range(cols):
                #if current cell is part of island, 
                #perform DFS & update area if it's larger than current max
                area = max(area, dfs(r, c)) 
        return area


