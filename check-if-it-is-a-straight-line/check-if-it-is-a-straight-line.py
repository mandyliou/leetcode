class Solution:
    def checkStraightLine(self, coor: List[List[int]]) -> bool:
        #slope = y2-y1 / x2-x1 = [1][1] - [0][1] / [1][0] - [0][0]
        # m = (coor[1][1] - coor[0][1]) / (coor[1][0] - coor[0][0])
        #this method will check for same ratio aka same slope
        x0, y0 = coor[0]
        x1, y1 = coor[1]

        for i in range(2, len(coor)):
            x, y = coor[i]
            #if ratio of diff is NOT constant, return False
            if ((x - x0) * (y1 - y0)) != ((y - y0) * (x1 - x0)):
                return False
        #all counter-example fall within the slope
        return True


