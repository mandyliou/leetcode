class Solution:
    def countBits(self, n: int) -> List[int]:
        new = [0] * (n + 1) # if n=2, it'll be [0, 0, 0]
        for i in range(1, n + 1): #iterates 1 to n
            new[i] = new[i >> 1] + (i & 1)
        return new


#new[1 >> 1] = 0 + 1 = 1
#new[2 >> 1] = 1 + 0 = 1
#new[3 >> 1] = 1 + 1 = 2
#new[4 >> 1] = new[2] = 1 + 0 = 1
#new[5 >> 1] = new[2] = 1 + 1 = 2

