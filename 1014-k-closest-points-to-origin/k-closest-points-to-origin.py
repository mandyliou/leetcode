from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [] # Initialize a max heap
        
        # Iterate through each point
        for point in points:
            dist = -(point[0]**2 + point[1]**2) # Calculate squared distance to origin, use negative for max heap
            heappush(max_heap, (dist, point)) # Push the distance and point into the heap
            if len(max_heap) > k: # If heap size exceeds k, remove the maximum element
                heappop(max_heap)
        
        # Extract the k closest points from the heap
        return [pair[1] for pair in max_heap]