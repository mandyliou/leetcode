#.sort():
#best case: O(n)
#average & worst case: O(n log n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]