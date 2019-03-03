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
class MyLinkedList:
    pass

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
