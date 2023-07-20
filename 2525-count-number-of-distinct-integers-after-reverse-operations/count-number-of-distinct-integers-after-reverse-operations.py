class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)): #must specify the original list or will keep looping
            rev = int(str(nums[i])[::-1]) #convert each ele to str, then reverse, & convert back to int
            nums.append(rev)
        return len(set(nums)) #gives num of distinct int