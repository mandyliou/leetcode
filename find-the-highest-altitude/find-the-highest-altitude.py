class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        add = [0] + [gain[0]]
        increment = 0 + gain[0] 
        for i in range(1, len(gain)):
            next_altitude = increment + gain[i]
            add.append(next_altitude)
            increment = next_altitude
        return max(add)