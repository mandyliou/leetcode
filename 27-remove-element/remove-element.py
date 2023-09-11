class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #assign 2 pointers
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == val: # If the current element is equal to val
                nums[i] = nums[n-1] #swap with the last element
                n -= 1 #reduce size of array
            else:
                i += 1 #move to next element
        return n





