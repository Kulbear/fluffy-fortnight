# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # Solution 1 - Hashmap
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = dict()
        step = 0
        while head:
            if head in s:
                return True
            s[head] = step
            head = head.next

        return False

    # Solution 2 - Two Pointers
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        # CRITICAL: check the stop condition
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
