class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0  #initial current altitude
        highest = 0
        for i in gain:
            curr += i #add new altitude to current altitude
            highest = max(highest, curr) #compares highest with current altitude & updates to new value
            
        return highest