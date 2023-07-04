class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]        
        if len(nums) == 2:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0] #if there's only 1 house, rob the only 1
        dp[1] = max(nums[0], nums[1]) #if there's 2 houses, pick the most $

        for i in range(2, len(nums)): #third house til end
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

           