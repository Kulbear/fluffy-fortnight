# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Solution 1 - DFS with Stack
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            node, val, left_sum = stack.pop()
            if not node.left and not node.right and val == 0:
                res.append(left_sum)
            if node.right:
                stack.append((node.right, val - node.right.val, left_sum + [node.right.val]))
            if node.left:
                stack.append((node.left, val - node.left.val, left_sum + [node.left.val]))
        return res
