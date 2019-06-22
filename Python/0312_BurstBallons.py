class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # ans = c[1][n]

        # 添加首尾虚拟气球
        n = len(nums)
        nums = [1] + nums
        nums.append(1)

        # 从气球 i 到 j 可得到的最大分数
        # dp[i][j] = maxCoins(nums[i:j + 1])
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        for l in range(1, n+1):  # l <= n, start from 1
            for i in range(1, n-l+2):  # i <= n-l+1, start from 1
                j = i + l - 1
                for k in range(i, j+1):  # k <= j, start from i
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1]
                                   * nums[k] * nums[j+1] + dp[k+1][j])

        return dp[1][n]
