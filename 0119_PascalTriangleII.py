class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1] * (i + 1) for i in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal[rowIndex]

    # Solution 2 - Recursion
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(row, col):
            if row == 0 or col == 0 or col == row:
                return 1
            else:
                return helper(row - 1, col - 1) + helper(row - 1, col)

        row = []
        for j in range(0, rowIndex + 1):
            row.append(helper(rowIndex, j))
        return row
