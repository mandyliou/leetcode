class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0]) 
        top = 0
        bottom = rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]: #target bigger than right most
                top = row + 1 
            elif target < matrix[row][0]: #target smaller than left most
                bottom = row - 1
            else: #target is in this row
                break
        if not (top <= bottom): #none of the rows have the target value
            return False
        row = (top + bottom) // 2 #runs it on the row we found
        l = 0
        r = columns - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False

        