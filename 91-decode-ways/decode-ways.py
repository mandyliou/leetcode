class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':  # Handle edge cases
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has one way to decode
        dp[1] = 1  # Single character string has one way to decode

        for i in range(2, n + 1):
            if s[i - 1] != '0':  # If the last digit is not zero
                dp[i] += dp[i - 1]

            two_digits = int(s[i - 2:i])
            if 10 <= two_digits <= 26:  # If the last two digits form a number between 10 and 26
                dp[i] += dp[i - 2]

        return dp[-1]
