class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} #create dict to store num and indices
        for i, n in enumerate(nums): #i = index, n = num
            diff = target - n #difference between target and curr num 
            if diff in d: #if diff exists in dict
                return [d[diff], i] #diff is found, return the indices of the 2 num
            d[n] = i #if diff does NOT exist, add curr num as key and index as value to dict

#time complexity: O(n) 
#n is length of nums List; iterates over list 1x
#space complexity: O(n)
#worst case all nums in list might need to be stored in dict