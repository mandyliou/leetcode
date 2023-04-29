class Solution:
    def countOdds(self, low: int, high: int) -> int:
        high = (high + 1) // 2 #finds odds between [1, high]
        low = low // 2 #finds odds between [1, low-1]
        return high - low #find odds [low, high] 