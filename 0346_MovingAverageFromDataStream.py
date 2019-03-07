from collections import deque


# Solution 1 - Queue
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.capacity = size
        self.size = 0
        self.sum = 0

    def next(self, val: int) -> float:
        if self.size < self.capacity:
            self.size += 1
            self.q.appendleft(val)
            self.sum += val
        else:
            head = self.q.pop()
            self.sum -= head
            self.sum += val
            self.q.appendleft(val)

        return self.sum / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
