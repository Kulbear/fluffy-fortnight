# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 - Recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node):
            if not node:
                return
            helper(node.left)
            lst.append(node.val)
            helper(node.right)

        lst = []
        helper(root)
        return lst

    # Solution 2 - Iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        lst = []
        cur = root
        stack = []
        while cur or stack:
            # go to deepest left
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            lst.append(cur.val)
            cur = cur.right

        return lst
