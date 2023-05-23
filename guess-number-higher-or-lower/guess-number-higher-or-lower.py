# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number; too big
#          1 if num is lower than the picked number; too small
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        while l <= h:
            mid = (l + h) // 2
            if guess(mid) > 0:
                l = mid + 1
            elif guess(mid) < 0:
                h = mid - 1
            else:
                return mid
        return -1

       
            
