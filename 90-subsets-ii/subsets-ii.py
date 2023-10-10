class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0, curr=[]):
            if start == len(nums):
                ans.add(tuple(curr))
                return
            # Include this number
            backtrack(start + 1, curr + [nums[start]])
            # Exclude this number
            backtrack(start + 1, curr)
        
        nums.sort()
        ans = set()
        backtrack()
        return [list(item) for item in ans]