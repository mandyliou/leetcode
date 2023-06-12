class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            end = nums[i]
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
                end = nums[i]
            result.append(f"{start}->{end}" if start != end else str(start))
            i += 1
        return result