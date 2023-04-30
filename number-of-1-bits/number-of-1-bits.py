class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_string = bin(n)[2:]
        return bin_string.count("1")