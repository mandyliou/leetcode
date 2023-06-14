class Solution:
    def isPalindrome(self, x: int) -> bool:
        #neg num will be false since it cant be palindrome
        new = []
        if x < 0: #negative number = false
            return False
        while x > 0:
            new.append(x % 10) #121%10 = 1; x = 12
            x = x // 10 # 12//10 = 1
        return new == new[::-1] #reverses it