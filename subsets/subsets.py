class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, end, subset):
            result.append(list(subset))
            for i in range(start, end):
                subset.append(nums[i])
                backtrack(i + 1, end, subset)
                subset.pop()
        backtrack(0, len(nums), [])
        return result

