class Solution:
    def checkStraightLine(self, coor: List[List[int]]) -> bool:
        #slope = y2-y1 / x2-x1 = [1][1] - [0][1] / [1][0] - [0][0]
        # m = (coor[1][1] - coor[0][1]) / (coor[1][0] - coor[0][0])
        #this method will check for same ratio aka same slope
        dy = coor[1][1] - coor[0][1] #dy= 3-2=1
        dx= coor[1][0] - coor[0][0] #dx=2-1=1
        for i in range(2, len(coor)):
            #if ratio of diff is NOT constant, return False
            if (dy * (coor[i][0] - coor[0][0])) != (dx * (coor[i][1] - coor[0][1])):
                return False
        #all counter-example fall within the slope
        return True

#1* (3-1)= 2
#1 * (4-2) = 2
