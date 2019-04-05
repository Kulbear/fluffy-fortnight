# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 - Recursive
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node):
            if not node:
                return

            lst.append(node.val)
            helper(node.left)
            helper(node.right)

        lst = []
        helper(root)
        return lst

    # Solution 2 - Iterative
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        lst = []
        stack = [root]
        while stack:
            cur = stack.pop()
            lst.append(cur.val)
            # CRITICAL: check right first as stack is FILO
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return lst
