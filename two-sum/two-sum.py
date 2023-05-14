class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new = {}
        #returns index and the value
        for i, n in enumerate(nums):
            #check if the n(number) is in dict already
            if n in new:
                #if it is, the 2 num that sum up to the target has been found; return the indices
                return [new[n], i]
            else: # add complement of current element to target to new as i as the key 
                new[target-n] = i
        return []