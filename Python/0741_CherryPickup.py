class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # if you go from top-left corner to bottom-right corner then come back
        # it is equivalent to have two path start from one of them to another
        # I suppose we have 2 "walker" start from the bottom right corner
        def step(x1, y1, x2, y2):
            # out of border
            if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
                return -1
            # -1 cell, cannot walk through
            if grid[y1][x1] < 0 or grid[y2][x2] < 0:
                return -1
            # reach the top-left corner
            if x1 == 0 and y1 == 0:
                return grid[y1][x1]
            # seen
            if dp[x1][y1][x2] != -1:
                return dp[x1][y1][x2]

            ans = max(
                max(step(x1 - 1, y1, x2 - 1, y2), step(x1, y1 - 1, x2, y2 - 1)),
                max(step(x1, y1 - 1, x2 - 1, y2), step(x1 - 1, y1, x2, y2 - 1))
            )

            if ans < 0:
                dp[x1][y1][x2] -= 1
                return dp[x1][y1][x2]
            ans += grid[y1][x1]
            if x1 != x2:
                ans += grid[y2][x2]

            dp[x1][y1][x2] = ans
            return ans

        n = len(grid)
        # we only need a 3D grid, because the 2 walker can only step together
        # given x1, y1 and x2 we can derive that y2 is always a unique value
        # y2 = x1 + y1 - x2
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]

        return max(0, step(n - 1, n - 1, n - 1, n - 1))
