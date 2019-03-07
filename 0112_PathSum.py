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

    # Solution 2 - Another Recursive
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        # leaf node
        if not root.left and not root.right:
            return sum == root.val

        left = False
        right = False
        left = left or self.hasPathSum(root.left, sum - root.val)
        right = right or self.hasPathSum(root.right, sum - root.val)

        return left or right

    # TODO: Solution 3 - Iterative
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        pass
