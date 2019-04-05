# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    # Solution 1 - Recursion with Hash Table
    def copyRandomList(self, head: Node) -> Node:
        def deepCopy(node):
            if node is None:
                return None

            # there will be cycle in the linked list
            # it's more like a graph
            # so the lookup dict also works as a visited map
            if node in lookup:
                return lookup[node]

            # create a new node for those we've never met before
            new = Node(node.val, None, None)
            lookup[node] = new

            new.next = deepCopy(node.next)
            new.random = deepCopy(node.random)

            return new

        # key (source node) : value (copied node)
        lookup = {}
        return deepCopy(head)

    # Solution 2 - Two-pass Iteration with Hash Table
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return
        lookup = {None: None}

        n = head
        while n:
            lookup[n] = Node(n.val, None, None)
            n = n.next

        n = head
        while n:
            lookup[n].next = lookup[n.next]
            lookup[n].random = lookup[n.random]
            n = n.next

        return lookup[head]

    # TODO: Solution 3 - One-pass Constant Space
    def copyRandomList(self, head: Node) -> Node:
        pass
