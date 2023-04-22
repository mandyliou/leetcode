class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]: #if the elements aren't equal, copy current element to left pointer  
                nums[l] = nums[r]
                l += 1

        return l
