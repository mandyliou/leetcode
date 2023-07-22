class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)#Divide by 10 and get n=quotient & digit=remainder
                total_sum += digit ** 2  # Square the remainder (digit) and add to total_sum
            return total_sum  # Return the total sum

        # Use a set to track seen numbers
        seen = set()
        # Loop until n is 1(happy number) or see a number that has already appeared (non-happy number)
        while n != 1 and n not in seen:
            seen.add(n)  # Add current number to seen set
            n = get_next(n)  # Get next number by squaring and adding digits
        return n == 1 #return true if num is happy aka 1
            
