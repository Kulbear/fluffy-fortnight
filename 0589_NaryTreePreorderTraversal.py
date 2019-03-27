"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []

        stack = [root]
        ans = []
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            # a stack is FILO so we need to reverse the children list
            # then the rightmost child will be put in the stack first
            # then it is visited as the last
            for child in reversed(cur.children):
                stack.append(child)

        return ans
