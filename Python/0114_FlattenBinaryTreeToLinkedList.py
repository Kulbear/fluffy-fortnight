# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 - Iterative DFS with Stack
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        last = TreeNode(-1)
        s = [root]
        while s:
            node = s.pop()
            last.right = node
            last.left = None
            if node and node.right:
                s.append(node.right)
            if node and node.left:
                s.append(node.left)
            last = node

    # TODO: Solution 2 - Recursion
    def flatten(self, root: TreeNode) -> None:
        pass
