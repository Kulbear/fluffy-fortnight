class Solution
{
  private:
    vector<vector<int>> dist;

  public:
    vector<vector<int>> updateMatrix(vector<vector<int>> &matrix)
    {
        vector<vector<int>> dist;

        if (matrix.empty() || matrix[0].empty())
            return dist;

        int rows = matrix.size();
        int cols = matrix[0].size();
        dist.resize(rows, vector<int>(cols, INT_MAX / 2));

        for (int i = 0; i < rows; ++i)
        {
            for (int j = 0; j < cols; ++j)
            {
                if (matrix[i][j] == 0)
                    dist[i][j] = 0;
                else
                {
                    if (j > 0)
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1);
                    if (i > 0)
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1);
                }
            }
        }

        for (int i = rows - 1; i > -1; --i)
        {
            for (int j = cols - 1; j > -1; --j)
            {
                if (j < cols - 1)
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1);
                if (i < rows - 1)
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1);
            }
        }

        return dist;
    }
};