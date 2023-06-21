import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            freq[i] += 1
        return heapq.nlargest(k, freq.keys(), key=freq.get)
        #1. k = want k of the largest elements to be returned
        #2. collection from largest elements to be selected -> freq.keys()
        #3. key function applied to each ele in iterable to determine sorting order -> freq.get 
            #for each ele in count.keys(), freq.get will return its count

#O(n * log k); n = num of elements; k = input parameter