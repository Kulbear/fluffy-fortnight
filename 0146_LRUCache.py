from collections import OrderedDict


# Solution 1 - OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        super().__init__(self)
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = super().get(key, -1)
        if value > 0:
            self.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# TODO: Solution 2 - Hash Table + Doubly Linked List
class LRUCache(OrderedDict):
    pass

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
