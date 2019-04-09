class Solution
{
  public:
    bool exist(vector<vector<char>> &board, string word)
    {
        h = board.size();
        w = board[0].size();
        for (int i = 0; i < w; ++i)
            for (int j = 0; j < h; ++j)
                if (search(board, word, i, j, 0))
                    return true;

        return false;
    }

  private:
    int w;
    int h;

    bool search(vector<vector<char>> &board, string word, int x, int y,
                int depth)
    {
        if (x < 0 || x >= w || y < 0 || y >= h || word[depth] != board[y][x])
            return false;
        if (depth == word.size() - 1)
            return true;

        char cur = board[y][x];
        board[y][x] = 0;

        bool found = search(board, word, x - 1, y, depth + 1) ||
                     search(board, word, x + 1, y, depth + 1) ||
                     search(board, word, x, y - 1, depth + 1) ||
                     search(board, word, x, y + 1, depth + 1);

        board[y][x] = cur;
        return found;
    }
};