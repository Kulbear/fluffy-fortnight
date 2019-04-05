# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Solution 1 - Iterative
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = head = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        head.next = l1 if l1 else l2

        return dummy.next

    # Solution 2 - Recursive
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # base case
        if None in (l1, l2):
            return l1 or l2

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            # don't forget the return
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # TODO: Solution 3 - In-Place Iterative
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode
        pass
