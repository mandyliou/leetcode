class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) #get size of matrix

        for row in range(n):
            for col in range(row, n):# For each row, iterate over each column starting from the diagonal.
                # Swap the element at (row, col) with the element at (col, row).
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for i in range(n): #reverse the rows
            matrix[i] = matrix[i][::-1]
        
        return matrix