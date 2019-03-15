class Solution:
    # Solution 1
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # empty matrix
        if len(matrix) == 0:
            return []

        # inital state
        r, c = len(matrix), len(matrix[0])
        top, right, bot, left = 0, c - 1, r - 1, 0
        trav = []

        while True:  # O(n)
            for i in range(left, right + 1):  # going right
                trav.append(matrix[top][i])
            top += 1
            if left > right or top > bot: break

            for i in range(top, bot + 1):  # going down
                trav.append(matrix[i][right])
            right -= 1
            if left > right or top > bot: break

            for i in range(right, left - 1, -1):  # going left
                trav.append(matrix[bot][i])
            bot -= 1
            if left > right or top > bot: break

            for i in range(bot, top - 1, -1):  # going up
                trav.append(matrix[i][left])
            left += 1
            if left > right or top > bot: break

        # in total O(n)
        return trav
