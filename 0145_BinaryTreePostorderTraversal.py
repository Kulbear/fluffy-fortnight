# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 - Recursive
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node):
            if not node:
                return

            helper(node.left)
            helper(node.right)
            lst.append(node.val)

        lst = []
        helper(root)
        return lst

    # Solution 2 - Iterative
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        lst = []
        stack = [root]
        while stack:
            cur = stack.pop()
            lst.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        lst.reverse()
        return lst
