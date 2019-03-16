class Solution:
    # Solution 1 - Recursion with Memorization
    def fib(self, N: int) -> int:
        def fib_mem(N, memory={0: 0, 1: 1}):
            if N <= 1:
                return memory[N]
            if N in memory:
                return memory[N]

            f = fib_mem(N - 2, memory) + fib_mem(N - 1, memory)
            memory[N] = f
            return f

        return fib_mem(N)
