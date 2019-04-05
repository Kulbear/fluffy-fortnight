class Solution:
    # Solution 1 - Brute Force
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        for _ in range(n):
            ans *= x
        return ans

    # Solution 2 - Recursion
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1

            half = helper(x, n // 2)
            if n % 2:
                return half * half * x
            return half * half

        if n < 0:
            x = 1 / x
            n = -n

        return helper(x, n)

    # Solution 3 - Iteration
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        cur = x
        while n > 0:
            if n % 2:
                ans = ans * cur
            cur *= cur
            n //= 2

        return ans
