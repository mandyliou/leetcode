class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = nums.copy()
        if len(nums) > 0:
            nums += new
        return nums
