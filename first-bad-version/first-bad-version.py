# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        bad = -1
        while low <= high:
            mid = (low + high) // 2
            potentialTrue = isBadVersion(mid)
            if potentialTrue: #true, equal or higher than bad
                bad = mid
                high = mid - 1
            else: #false; too low compared to bad
                low = mid + 1
        return bad