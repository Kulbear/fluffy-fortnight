# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Solution 1 - Iterative
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur:
            # store the next one
            temp = cur.next
            # connect cur with prev
            # this step is similar to add at head
            # prev is the reversed part
            cur.next = prev
            # cur becomes prev, move on
            prev = cur
            # cur becomes the head of unfinished part
            cur = temp

        return prev

    # Solution 2 - Recursive
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return p
