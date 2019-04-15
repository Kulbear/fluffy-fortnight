import random

# Solution 1 - Hash Map and List
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        self.map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False
        # idx is the to-delete value index in arr
        # last is the last value in the arr
        idx, last = self.map[val], self.arr[-1]
        # set the value at to-delete index to the last value in arr
        # set the idx of the last value in arr in map to the new idx
        # note the new idx is the idx of the to-delete value
        self.arr[idx], self.map[last] = last, idx
        self.arr.pop()
        self.map.pop(val, 0)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[random.randint(0, len(self.arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
