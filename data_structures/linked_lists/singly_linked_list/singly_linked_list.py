class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyListLlist:
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

