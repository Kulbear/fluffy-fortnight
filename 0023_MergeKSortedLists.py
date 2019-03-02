# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Solution 1 - Heap (Priority Queue)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = head = ListNode(0)
        heap = []

        # CRITICAL: add comparability to elements in the heap
        step = 0
        for lst in lists:
            while lst:
                heapq.heappush(heap, (lst.val, step, lst))
                lst = lst.next
                step += 1

        while heap:
            head.next = heapq.heappop(heap)[-1]
            head = head.next

        return dummy.next

    # Solution 2 - Merge Sort
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def merge(list1: List[ListNode], list2: List[ListNode]) -> ListNode:
            dummy = head = ListNode(0)
            # it's just the merge in merge sort
            while list1 and list2:
                if list1.val > list2.val:
                    head.next = list2
                    list2 = list2.next
                else:
                    head.next = list1
                    list1 = list1.next
                # CRITICAL: proceed after finish
                head = head.next

            # connect the rest
            head.next = list1 if list1 else list2

            return dummy.next

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return merge(left, right)
