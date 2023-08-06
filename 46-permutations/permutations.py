from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def backtrack(current_permutation):
            if len(current_permutation) == len(nums): # If permutation is of the same length as the original array, add a copy of perm to the results
                results.append(current_permutation[:])
                return

            for num in nums: # Try to add each num to  current permutation
                if num not in current_permutation:
                    current_permutation.append(num) # Add the number
                    # Recursively generate permutations for the remaining num
                    backtrack(current_permutation)
                    current_permutation.pop() # Remove the number to backtrack

        results = []
        backtrack([])
        return results
