class Solution:
    # Solution 1 - Dynamic Programming
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [1] * n
        dp[1] = 2
        if n < 2:
            return dp[n]
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[-1]

    # Solution 2 - Recursion with Memorization
    def climbStairs(self, n: int) -> int:
        def climb(n, memory={0: 0, 1: 1, 2: 2}):
            if n <= 2:
                return memory[n]

            if n in memory:
                return memory[n]

            memory[n] = climb(n - 2, memory) + climb(n - 1, memory)
            return memory[n]

        return climb(n)
