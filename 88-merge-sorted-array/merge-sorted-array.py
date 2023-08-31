class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1 # p1 points to the end of the meaningful elements in nums1
        p2 = n - 1 # p2 points to the end of nums2
        p = m + n - 1 # p points to the end of the entire nums1 list
        
        while p1 >= 0 and p2 >= 0: #Traverse both arrays from end towards beginning
            if nums1[p1] > nums2[p2]: # If element at p1's greater than the element at p2
                nums1[p] = nums1[p1] # Place the element at p1 in the merged position p
                p1 -= 1
            else:# Otherwise, place the element at p2 in the merged position p
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1 # Decrement  merged position pointer p

        # If nums2 still has elements left, copy them over to nums1
        # This step's needed bc if nums2 has the smallest elements, they won't be placed in nums1 yet
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1