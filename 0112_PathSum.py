# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Solution 1 - Recursive
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:  # if reach a leaf
            return sum == root.val

        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    # TODO: Solution 2 - Iterative
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        pass
