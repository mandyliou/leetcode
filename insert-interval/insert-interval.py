class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in intervals:
            if newInterval[1] < i[0]: #if new intv comes before curr intv
                result.append(newInterval)
                newInterval = i
            elif newInterval[0] > i[1]: #new intv is after curr intv
                result.append(i)
            else: #new intv overlaps/ within range of other interval; 
            #UPDATE, min for start & max for end
                newInterval[0] = min(i[0], newInterval[0])
                newInterval[1] = max(i[1], newInterval[1])

        result.append(newInterval)
        return result 