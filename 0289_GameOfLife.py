class Solution:
    # Solution 1 - State Transfer
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        r, c = len(board), len(board[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        for i in range(r):
            for j in range(c):
                lives = 0
                for m, n in neighbors:
                    if 0 <= i + m < r and 0 <= j + n < c:
                        lives += board[i + m][j + n] & 1

                if board[i][j] and 2 <= lives < 4:
                    board[i][j] = 3

                if not board[i][j] and lives == 3:
                    board[i][j] = 2

        for i in range(r):
            for j in range(c):
                board[i][j] >>= 1
