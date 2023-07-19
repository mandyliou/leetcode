class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse(x: int) -> int: # helper function to reverse a number
            # str(x)[::-1] reverses string; int() turns it back into an integer
            return int(str(x)[::-1])

        # reverse the number twice; return True if the twice-reversed number is the same as the original number; otherwise return False
        return num == reverse(reverse(num))