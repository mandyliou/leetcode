class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length #creates empty list same size as nums
        answer[0] = 1 #initialize 1st ele of answer as 1, since no ele to the left of it in input list
        for i in range(1, length): #starts from 2nd element(1st index) until the last
            answer[i] = nums[i-1] * answer[i-1] #calculates products to the left of nums
        R = 1 #R will store all elements to the right
        for i in reversed(range(length)): #will go from last ele to 1st ele in nums
            answer[i] = answer[i] * R #will update product in each index
            R *= nums[i] #R is updated by multiplying it with nums[i]; will have all product to the right
        return answer #updated 'answer' array will have all products minus own index


