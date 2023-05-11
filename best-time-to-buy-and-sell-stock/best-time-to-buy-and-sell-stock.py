class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf') #basically set to infinity

        for i in prices:
            min_price = min(min_price, i) #finds lowest price so far
            profit = i - min_price #potential profit
            max_profit = max(max_profit, profit) #finds max profit
        return max_profit
