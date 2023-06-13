from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = set() #set is for fresh oranges
        q = deque() #queue holds all positions of rotten oranges
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: #add rotten orrange to queue
                    q.append((r, c))
                if grid[r][c] == 1: #fresh orange, increase by 1 count
                    fresh.add((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0 #initial is 0 min
        while q and fresh: #while there are still rotten and fresh oranges
            for _ in range(len(q)): #iterate for each rotten orange in queue
                r, c = q.popleft() #removing rotten orange from q, and assign to r & c
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if ((new_r, new_c) in fresh  #if adjacent orange is fresh
                    and 0 <= new_r < rows # && within boundaries
                    and 0 <= new_c < cols):                
                        fresh.remove((new_r, new_c)) #remove it from fresh set
                        q.append((new_r, new_c)) #add to rotten queue
            time += 1 #increment time after each min of rotting

        #if there are still fresh oranges left, return -1
        #otherwise, return the total elapsed time
        return -1 if fresh else time

            
            
