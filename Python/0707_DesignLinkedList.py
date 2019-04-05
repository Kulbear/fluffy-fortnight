# Solution 1 - Singly Linked List
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # empty or out of bound
        if self.size == 0 or index >= self.size:
            return -1

        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1

        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new = ListNode(val)
        new.next = self.head
        self.head = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.size == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            # iterate to the tail
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # add to tail
        if index == self.size:
            self.addAtTail(val)
            return

        # out of bound, invalid
        if index > self.size:
            return

        # add to head
        if index == 0:
            self.addAtHead(val)
            # CRITICAL: avoild duplicated size++
            return

        prev = None
        cur = self.head
        while index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        prev.next = ListNode(val)
        prev.next.next = cur
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # invalid
        if index >= self.size:
            return

        # remove head
        if index == 0:
            self.head = self.head.next
            return

        prev = None
        cur = self.head
        while index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        prev.next = cur.next

        self.size -= 1


# Solution 2 - Doubly Linked List
class DListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.val)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # index out of range
        if index >= self.size:
            return -1

        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = DListNode(val)
        node.next = self.head
        # equivalent to if self.size > 0
        if self.head:
            self.head.prev = node
        self.head = node
        # equivalent to if self.size == 0
        if not self.tail:
            self.tail = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.size == 0:
            self.addAtHead(val)
        else:
            node = DListNode(val)
            # just connect to tail and link the references...
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:  # index out of range
            return
        if index == self.size:
            self.addAtTail(val)
        else:
            node = self.head
            for _ in range(index):
                node = node.next
            prev = node.prev
            if not prev:
                self.addAtHead(val)
            else:
                new = DListNode(val)
                prev.next = new
                new.prev = prev
                new.next = node
                node.prev = new
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return

        node = self.head
        for _ in range(index):
            node = node.next

        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        else:
            self.tail = prev
        self.size -= 1

    def __str__(self):
        node = self.head
        s = ''
        while node:
            s += str(node.val)
            s += ' -> '
            node = node.next

        return s

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
