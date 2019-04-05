class Solution:
    # Solution 1 - Iteration
    def generate(self, numRows: int) -> List[List[int]]:
        # create the final output container
        pascal = [[1] * (i + 1) for i in range(numRows)]
        # once we finish a row we can use it for the future rows and we never change it anymore
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal

    # Solution 2 - Recursion
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(row, col):
            if row == 0 or col == 0 or col == row:
                return 1
            else:
                return helper(row - 1, col - 1) + helper(row - 1, col)

        output = []
        for i in range(numRows):
            row = []
            for j in range(0, i + 1):
                row.append(helper(i, j))
            output.append(row)
        return output
