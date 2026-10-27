class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size: int = 0

    # To get the length of the linked list
    def __len__(self):
        return self.size

    # TO print the entire linked linked in a readable format
    def __str__(self):
        if self.head is None:
            return "Empty list"

        linkedlist = ""
        current = self.head
        while current and current.next is not None:
            linkedlist += str(current.element) + "->"
            current = current.next

        linkedlist += str(current.element)
        return linkedlist

    # Adding a new node to the head of the linked list and this will become the new head
    def addFirst(self, element):
        newHead = Node(element)
        newHead.next = self.head
        self.head = newHead

        if self.tail is None:
            self.tail = self.head

        self.size += 1

    def addLast(self, element):
        newNode = Node(element)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

        # The code below will have a time complexity of O(n) because we are traversing from the head
        # node = self.head
        # while node.next is not None:
        #     node = node.next
        # node.next = Node(element)
        # self.tail = node.next
        # self.size += 1

    def addAtPosition(self, position, element):
        if position < 1 or position > self.size + 1:
            raise IndexError("Position is invalid")

        if position == 1:
            self.addFirst(element)
            return

        index = 1
        prev = None
        current = self.head
        newNode = Node(element)

        while index != position:
            index += 1
            prev = current
            current = current.next

        prev.next = newNode
        newNode.next = current

        self.size += 1

    def removeFirst(self):
        if self.head is None:
            raise IndexError("cannot remove from an empty list")

        nodeToRemove = self.head

        if self.head.next is None:
            self.head = self.tail = None
            self.size = 0
            return nodeToRemove.element

        self.head = self.head.next

        self.size -= 1

        return nodeToRemove.element

    def removeLast(self):
        if self.head is None:
            raise IndexError("Cannot remove from an empty list")

        nodeToRemove = self.tail

        if self.head.next is None:
            self.head = self.tail = None
            self.size = 0
            return nodeToRemove.element

        prev = None
        current = self.head

        while current.next is not None:
            prev = current
            current = current.next

        prev.next = None
        self.tail = prev

        self.size -= 1

        return nodeToRemove.element


    def removeAtPosition(self, position):
        if position < 1 or position > self.size:
            raise IndexError("Invalid position")

        if position == 1:
            return self.removeFirst()

        if position == self.size:
            return self.removeLast()

        index = 1
        prev = None
        current = self.head

        while index != position:
            index += 1
            prev = current
            current = current.next

        prev.next = current.next

        self.size -= 1

        return current.element