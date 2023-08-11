class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize pointers: p0: rightmost boundary for zeros ; p2: leftmost boundary for twos; # curr: current pointer for traversal
        p0, curr = 0, 0
        p2 = len(nums) - 1
        
        # While current pointer doesn't cross p2
        while curr <= p2:
            
            if nums[curr] == 0: # If current element is 0
                nums[p0], nums[curr] = nums[curr], nums[p0] # Swap current element with element at p0
                # Move p0 and curr pointers to the right
                p0 += 1
                curr += 1
            elif nums[curr] == 2: # If current element is 2
                nums[curr], nums[p2] = nums[p2], nums[curr]# Swap current element with element at p2
                # Move p2 pointer one step to the left
                p2 -= 1
            else:  # If current element is 1, just move the current pointer
                curr += 1

        return nums

    # Time : O(N)  N is the length of the nums array.
    # Space : O(1) since no extra space is used except for a few variables.