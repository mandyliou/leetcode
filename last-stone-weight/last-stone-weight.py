class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:#[2,7,4,1,8,1]
        stones_neg = []
        for i in stones:
            stones_neg.append(-i) #negate value to use max-heap; [-2,-7,-4,-1,-8,-1]
        heapq.heapify(stones_neg) #turn array to heap, heaviest is at root [-8,-7,-4,-2,-1,-1]

        while len(stones_neg) > 1: #want at least 2 stones
            stone1 = -heapq.heappop(stones_neg) #pop heaviest stone, and make positive; 8
            stone2 = -heapq.heappop(stones_neg) #pop 2nd heaviest stone; 7
            if stone1 > stone2:
                heapq.heappush(stones_neg, -(stone1 - stone2)) #-(8-7)=-1; so [-4,-2,-1,-1,-1]

        stones_neg.append(0) #empty list, return 0
        return -stones_neg[0] #not empty, return last stone weight

