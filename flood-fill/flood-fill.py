class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == color:
            return image
        rows = len(image)
        cols = len(image[0])
        def dfs(r, c):
        #if current pixel's out of bounds, or current cell is same color -> return
            if (r < 0 or c < 0) or (r >= rows or c >= cols) or (image[r][c] != oldColor):
                return
            #mark current cell as 0 if it's been visited
            image[r][c] = color #color current pixel with new color
            dfs(r + 1, c) #down
            dfs(r - 1, c) #up
            dfs(r, c + 1) #right
            dfs(r, c - 1) #left
        dfs(sr, sc)
        return image