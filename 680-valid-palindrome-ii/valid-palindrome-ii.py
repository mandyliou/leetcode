class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 #pointer 1
        r = len(s) - 1 #pointer 2
        while l < r: #compare indices, should never be equal/same
            if s[l] == s[r]: #if both are same, increment the values
                l += 1
                r -= 1
            else: #if not the same, compare 1) without the last value vs reverse 2) without the first value vs reverse
                return s[l:r] == s[l:r][::-1] \
                or s[l+1:r+1] == s[l+1:r+1][::-1]
        return True #if both end values are same