class Solution:
    # Solution 1 - Recursive DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            # grid[x][y] != '1' means visited or water
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != '1':
                return
            grid[x][y] = '0'
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count

    # TODO: Solution 2 - Union Find
    def numIslands(self, grid: List[List[str]]) -> int:
        pass
