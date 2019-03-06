# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 - Recursive
    def isSymmetric(self, root: TreeNode) -> bool:
        # empty tree
        if not root:
            return True

        def helper(left, right):
            # called from a leaf node
            if not left and not right:
                return True
            # the pair missing one node, 100% false
            if not left or not right:
                return False

            #             1
            #           /   \
            #          2     2
            #         / \   / \
            #        3   4 4   3
            # suppose left is 2, right is another 2
            # then you get what is inner what is outer
            if left.val == right.val:
                inner = helper(left.right, right.left)
                outer = helper(left.left, right.right)
                return inner and outer
            # not equal
            else:
                return False

        # start from level 2 you always need to check a pair of nodes
        return helper(root.left, root.right)

    # TODO: Solution 2 - Iterative
    def isSymmetric(self, root: TreeNode) -> bool:
        pass
