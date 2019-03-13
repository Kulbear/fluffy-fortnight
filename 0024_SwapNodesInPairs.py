# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Solution 1 - Recursion
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # think about 1 -> 2 -> 3 -> 4
        # temp is 2, head is 1
        temp = head.next
        # connect 1's next to swapped linkedlist starting at 3
        head.next = self.swapPairs(head.next.next)
        # connect 2's next to 1 (2 -> 1 -> recursion)
        temp.next = head

        return temp
