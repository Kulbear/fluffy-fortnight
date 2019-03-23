class Solution:
    # Solution 1 - Dynamic Programming
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:  # top-left corner
                    continue
                elif i == 0 and j != 0:  # top row
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:  # left column
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]

        return grid[-1][-1]
