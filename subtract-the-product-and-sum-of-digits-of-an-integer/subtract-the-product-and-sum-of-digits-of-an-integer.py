class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        new = [int(i) for i in str(n)]
        for j in new:
            product *= j
            sum += j
        return product - sum
        
        