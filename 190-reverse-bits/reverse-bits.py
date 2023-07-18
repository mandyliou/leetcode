class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32): # Iterating over 32 bits
            result <<= 1 # Shift result left to make room for the new bit
            result |= n & 1 # Add the least significant bit of n to result
            n >>= 1 # Shift n right to discard the least significant bit
        return result

 