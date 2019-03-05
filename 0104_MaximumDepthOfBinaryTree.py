# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 - Top-down Approach
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        def helper(node, depth):
            if not node:
                return
            ans[0] = max(ans[0], depth)
            # knowing some param from current level
            # pass it to the next level
            # this is top-down
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        ans = [1]
        helper(root, 1)
        return ans[0]

    # Solution 2 - Bottom-top Approach
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # we start to going to the top from the bottom (left node)
        if not root.left and not root.right:
            return 1

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
