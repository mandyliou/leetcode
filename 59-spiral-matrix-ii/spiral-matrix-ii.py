class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
          # Initialize a n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]

        # Define initial boundaries for the spiral
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1  # Start filling from 1

        # Spiral filling
        while left <= right and top <= bottom:
            # Fill the top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # Fill the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Fill the bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            # Fill the left column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix
