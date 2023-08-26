class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array where dp[i] reps the min num of coins required to make amount i.
        # Initialize each position with a large value, 'amount+1' (which is an impossible maximum value), for upcoming min comparison.
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # Base Case: The number of coins required for amount 0 is 0.
        for coin in coins: #loops thru for each coin
            for i in range(coin, amount + 1): # For each coin, update dp values from 'coin' to 'amount'.
                dp[i] = min(dp[i], dp[i - coin] + 1)# check if current coin leads to a solution with fewer coins.
        # If dp[amount] has a value <= amount, it means we found a solution. 
        # Otherwise, it means there's no combination 
        return dp[amount] if dp[amount] <= amount else -1
