class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        A = [-prices[0] for _ in prices]  # can sell
        B = [-float('inf') for _ in prices]  # can only rest
        C = [0 for _ in prices]  # can buy

        for i in range(1, len(prices)):
            A[i] = max(A[i - 1], C[i-1] - prices[i])
            B[i] = A[i - 1] + prices[i]
            C[i] = max(C[i-1], B[i-1])

        return max(B[len(prices) - 1], C[len(prices) - 1])
