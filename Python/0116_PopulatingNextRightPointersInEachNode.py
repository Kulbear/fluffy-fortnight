"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        pre = root
        cur = None

        # always use pre to keep track of the left most node at each level
        while pre.left:
            cur = pre
            while cur:
                # connect left and right children
                cur.left.next = cur.right
                # connect right child and the left child of the next node at the same level
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            # move on to the next level
            pre = pre.left

        return root
