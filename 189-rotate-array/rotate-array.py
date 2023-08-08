class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k > n

        def reverse(start, end):  # Helper function to reverse a sub-array
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n-1)  # Reverse the entire array
        reverse(0, k-1) # Reverse the first k elements
        reverse(k, n-1) # Reverse the remaining n-k elements
