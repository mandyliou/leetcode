class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1): 
            temp = one
            one = one + two #add 2 prev values
            two = temp #gets shifted to w/e one was
        return one

