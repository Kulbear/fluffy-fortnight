# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 - Recursion
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left

        return root

    # TODO: Solution 2 - Iteration with Queue
    def invertTree(self, root: TreeNode) -> TreeNode:
        pass
