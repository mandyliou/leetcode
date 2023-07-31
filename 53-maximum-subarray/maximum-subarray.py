class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: #if list is empty, return 0
            return 0
        #initialize current sum and max sum to the first number in the list
        current_sum = nums[0] 
        max_sum = nums[0]
        for i in nums[1:]: #iterate thru list from 1st num to the end
            current_sum = max(i, current_sum + i) #for e/ num, calculate current sum, either num itself or num from previous sum 
            max_sum = max(max_sum, current_sum) #update max sum, if current sum is greater than max sum 
        return max_sum #return max sum found
