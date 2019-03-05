# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 - Iterative
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        lst = []
        queue = [root]
        while queue:
            lv_lst = []
            for i in range(len(queue)):
                node = queue.pop(0)
                lv_lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lst.append(lv_lst)

        return lst
