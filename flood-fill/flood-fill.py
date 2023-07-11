class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Store the original color of the starting pixel
        oldColor = image[sr][sc]
        
        # If the original color is the same as the new color, no changes are needed
        # so we return the original image
        if oldColor == color:
            return image

        # Get the dimensions of the image
        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # If the current pixel is out of the image boundaries or the color 
            # of the current pixel is not the same as the original color, return
            if (r < 0 or c < 0) or (r >= rows or c >= cols) or (image[r][c] != oldColor):
                return

            # Change the color of the current pixel to the new color
            image[r][c] = color

            # Perform a depth-first search on the 4 neighbouring pixels
            dfs(r + 1, c) # Move down
            dfs(r - 1, c) # Move up
            dfs(r, c + 1) # Move right
            dfs(r, c - 1) # Move left

        # Start the depth-first search from the starting pixel
        dfs(sr, sc)
        
        # Return the modified image after performing the flood fill
        return image
