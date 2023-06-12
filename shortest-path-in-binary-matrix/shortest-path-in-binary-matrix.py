from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set([(0, 0)]) #add starting cell to visited
        queue = deque([(0, 0, 1)]) #queue holds coor of the cells to visit next, along with steps taken 
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        #if start or end is blocked(1), return -1
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        while queue: #queue not empty
            #remove first cell from queue & get the coor along w/ 
            #length = num of steps taken to reach it
            r, c, length = queue.popleft()
            if r == rows - 1 and c == cols - 1: #if bottom right cell, found path
                return length
            for dr, dc in neighbors: #for each possible directions..
                #calculate coor of next cell
                nr = r + dr
                nc= c + dc

                if (rows > nr >= 0) and (cols > nc >= 0) and (grid[nr][nc] == 0) and ((nr,nc) not in visit):
                    queue.append((nr, nc, length + 1))
                    visit.add((nr, nc))
        return -1 


                

