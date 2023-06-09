class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #hashmap
        new = {}
        for i in nums:
            if i not in new:
                new[i] = 1
            else:
                new[i] += 1
                return True        