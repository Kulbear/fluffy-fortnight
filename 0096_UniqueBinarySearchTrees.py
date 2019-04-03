class Solution:
    # Solution 1 - Dynamic Programming
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for rt in range(i):
                dp[i] += dp[rt] * dp[i - 1 - rt]
        return dp[n]
