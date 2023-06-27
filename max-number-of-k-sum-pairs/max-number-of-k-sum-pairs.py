from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Use Counter to get a dictionary with counts of each number in nums
        count = Counter(nums)
        operations = 0  # Initialize counter for operations
        
        # Iterate over each number in nums
        for num in nums:
            # If both num and k - num are present in the array
            if count[num] > 0 and count[k - num] > 0:
                # If num is equal to k - num, there should be at least 2 counts of num
                if num == k - num and count[num] < 2:
                    continue
                # Decrement counts for num and k - num
                count[num] -= 1
                count[k - num] -= 1
                # Increment operations
                operations += 1
                
        return operations
