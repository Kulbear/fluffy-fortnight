# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result

        container = deque([root])
        left2right = True

        # Think about this tree
        #   3
        #  / \
        # 9  20
        #   /  \
        #  15   7
        while container:
            level = []
            # imagine this is the frist time we are here, say this is
            # Round 1: container = [3], left2right = True
            # Round 2: container = [9, 20], left2right = False
            # Round 3: omitted...
            for _ in range(len(container)):
                if left2right:  # works as a queue
                    # Round 1: container = [3], traverse from left to right
                    cur = container.popleft()  # we get 3 here
                    level.append(cur.val)
                    if cur.left:
                        container.append(cur.left)
                    if cur.right:
                        container.append(cur.right)
                    # Round 1: End up with container = [9, 20], remember we need to traverse from right
                else:  # works as a stack
                    # Round 2: container = [9, 20], traverse from right to left
                    cur = container.pop()  # we get 20 here
                    level.append(cur.val)
                    # Round 2 (CRITICAL): append from left side, so need to append right first
                    if cur.right:
                        container.appendleft(cur.right)
                    if cur.left:
                        container.appendleft(cur.left)
                    # Round 2 (CRITICAL): container = [15, 7], remember next time we will traverse from left to right
            left2right = not left2right  # zigzag it...
            result.append(level)

        return result
