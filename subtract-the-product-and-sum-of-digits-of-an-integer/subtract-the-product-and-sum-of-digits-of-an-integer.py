class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        new = []
        product = 1
        sum = 0
        for i in str(n):
            new.append(int(i))
        for j in new:
            product *= j
            sum += j
        return product - sum
        
        