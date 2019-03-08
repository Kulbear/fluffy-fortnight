from collections import deque


class Solution:
    # Solution 1 - Recursive DFS
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def dfs(x, y, dist):
            # CRITICAL: rooms[x][y] < dist solves too many edge cases!
            if x < 0 or y < 0 or x >= len(rooms) or y >= len(rooms[0]) or rooms[x][y] < dist:
                return
            rooms[x][y] = dist
            dist += 1
            dfs(x + 1, y, dist)
            dfs(x, y + 1, dist)
            dfs(x - 1, y, dist)
            dfs(x, y - 1, dist)

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)

    # Solution 2 - Iterative Top-Down BFS
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        h = len(rooms)
        w = len(rooms[0])

        q = deque()
        for i in range(h):
            for j in range(w):
                # record search start point
                if rooms[i][j] == 0:
                    # enqueue
                    q.append((i, j))

        while q:
            # dequeue
            row, col = q.popleft()
            # this is similar to top-down approach
            dist = rooms[row][col] + 1
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dy
                c = col + dx
                if 0 <= r < h and 0 <= c < w:
                    if dist < rooms[r][c]:
                        rooms[r][c] = dist
                        q.append((r, c))
