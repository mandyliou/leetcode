class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x) #convert int to str for bit manipulation
        if x < 0: # Check if the number is negative
            str_x = str_x[1:] # Remove the "-" sign from the start
            # Reverse the remaining string and add the "-" sign back to the start
            result = int('-' + str_x[::-1])
        else: # If the number is positive, just reverse the string
            result = int(str_x[::-1])
            
        # Define the range of a 32-bit signed integer
        mina = -2**31
        maxa = 2**31 - 1
        
        if result not in range(mina, maxa): # Check if result is w/in the range
            # If it's outside the range, return 0 as per the problem's requirement
            return 0
        else: # if in range, return result
            return result