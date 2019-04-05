from heapq import heapify, heappush, heappop


# Solution 1 - Heap
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []  # max heap (use neg)
        self.r = []  # min heap (default)
        heapify(self.l)
        heapify(self.r)

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # min/max heap trick
        if len(self.l) == 0 or num < -self.l[0]:
            heappush(self.l, -num)
        else:
            heappush(self.r, num)

        if len(self.l) < len(self.r):
            heappush(self.l, -heappop(self.r))
        elif len(self.l) - len(self.r) == 2:
            heappush(self.r, -heappop(self.l))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.l) > len(self.r):
            return -self.l[0]
        else:
            return (-self.l[0] + self.r[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
