class Solution:
    # Solution 1 - Sliding Window Scan
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        island = 0
        neighbor = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    island += 1
                    # down neighbor
                    if i < len(grid) - 1 and grid[i + 1][j]:
                        neighbor += 1
                    # right neighbor
                    if j < len(grid[i]) - 1 and grid[i][j + 1]:
                        neighbor += 1

        return island * 4 - 2 * neighbor
