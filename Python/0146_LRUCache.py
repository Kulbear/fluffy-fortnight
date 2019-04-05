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


# Solution 2 - Hash Table + Doubly Linked List
class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        # update to the tail
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key, value)
        # update to the tail
        self.append(node)
        self.hashmap[key] = node

        # check capacity
        if len(self.hashmap) > self.capacity:
            head = self.head.next
            # remove the least recently used
            self.remove(head)
            self.hashmap.pop(head.key)

    def append(self, node: Node) -> None:
        """Append a new node to the end of the doubly linked list (before the dummy tail)"""
        tail = self.tail.prev
        tail.next = node
        node.prev = tail
        self.tail.prev = node
        node.next = self.tail

    def remove(self, node: Node) -> None:
        """Remove a specified node, obtained from the hashmap."""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
