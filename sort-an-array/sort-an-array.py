class Solution:
    def sortArray(self, nums):
        def mergesort(arr):
            if len(arr) <= 1: #base case 1 or zero element
                return arr
            mid = len(arr) // 2 #split array in halves
            left = mergesort(arr[:mid]) #sort left half
            right = mergesort(arr[mid:]) #sort right half
            return merge(left, right) #merge two sorted halves and return result

        def merge(left, right): #combine 2 sorted arrays into 1 array
            merged = []
            i = j = 0
            while i < len(left) and j < len(right): 
                if left[i] <= right[j]: #if val in left array is smaller, append
                    merged.append(left[i])
                    i += 1 #moves onto next element of left array
                else: #if val in right array is smaller, append 
                    merged.append(right[j])
                    j += 1 #moves onto next ele of right array
            
            #takes care of leftover elements
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged
        return mergesort(nums) #need to call mergesort fxn to return sorted array

