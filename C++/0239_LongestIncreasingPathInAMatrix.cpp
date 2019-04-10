class Solution
{
  private:
    vector<vector<int>> dp;
    int height = 0, width = 0;
    int dfs(vector<vector<int>> &matrix, int cur, int i, int j)
    {
        // out of bound and not increasing
        if (i < 0 || i >= height || j < 0 || j >= width || matrix[i][j] <= cur)
            return 0;
        if (dp[i][j] > 0)
            return dp[i][j];
        int r = dfs(matrix, matrix[i][j], i + 1, j);
        int l = dfs(matrix, matrix[i][j], i - 1, j);
        int u = dfs(matrix, matrix[i][j], i, j + 1);
        int d = dfs(matrix, matrix[i][j], i, j - 1);
        dp[i][j] = max({r, l, u, d}) + 1;
        return dp[i][j];
    }

  public:
    int longestIncreasingPath(vector<vector<int>> &matrix)
    {
        if (matrix.empty() || matrix[0].empty())
            return 0;
        height = matrix.size(), width = matrix[0].size();
        dp.resize(height, vector<int>(width));
        int max_len = 0;
        for (int i = 0; i < height; ++i)
            for (int j = 0; j < width; ++j)
                max_len = max(max_len, dfs(matrix, INT_MIN, i, j));
        return max_len;
    }
};