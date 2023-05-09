class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #convert bin string into int: int()
        #sum of a and b
        #convert int into bin string: bin()
        a, b = int(a, 2), int(b, 2)
        int_sum = a + b
        return bin(int_sum)[2:]