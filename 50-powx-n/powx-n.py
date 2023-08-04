class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:  # Base case: anything to the power of 0 is 1
            return 1
        if n < 0:  # If n is negative, invert x and make n positive
            x = 1 / x
            n = -n

        result = 1  # Initialize the result

        # Loop until n becomes zero
        while n > 0:
            if n % 2:  # If n is odd, multiply result by x
                result *= x
            x *= x  # Square x at each step
            n //= 2  # Halve n at each step, using integer division

        return result  