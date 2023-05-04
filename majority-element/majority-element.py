class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occur = set(nums)
        return max(occur, key=nums.count)