# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Solution 1 - Hash Table
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        s = set()
        while p1:
            s.add(p1)
            p1 = p1.next
        while p2:
            if p2 in s:
                return p2
            s.add(p2)
            p2 = p2.next

        return

    # Solution 2 - Two Pointers
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        p1, p2 = headA, headB
        # the idea is to traverse simultaneously the two linked list if there is an intersection node
        # say 1 - 2 - 3
        #              \
        #               4 - 5 - 6
        #              /
        #         a - b
        # they meet at 4
        # say p1 start at node 1 and p2 start at node a
        # every iteration p1 and p2 will proceed one step and p2 first reached the end
        # headA (node 1) is assigned to p2
        # so when they meet
        # p1 has done a path 1 - 2 - 3 - 4 - 5 - 6 - a - b - 4
        # p2 has done a path a - b - 4 - 5 - 6 - 1 - 2 - 3 - 4
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA

        return p1
