# Singly Linked List in Python

A clean, efficient implementation of a **Singly Linked List** built from scratch in Python.

Unlike standard singly linked lists that only track the head pointer, this implementation maintains both **`head`** and **`tail`** pointers, enabling optimized **`O(1)` constant-time insertion** at the end of the list.

---

##  Features & Implemented Methods

| Method | Description | Time Complexity |
|---|---|---|
| `__init__()` | Initializes an empty list with `head = None`, `tail = None`, and `size = 0`. | `O(1)` |
| `__len__()` | Returns the total number of nodes using Python's built-in `len()`. | `O(1)` |
| `__str__()` | Returns a human-readable string representation (e.g., `10->20->30`). | `O(n)` |
| `addFirst(element)` | Inserts a new node at the head of the list. | `O(1)` |
| `addLast(element)` | Appends a new node to the tail using the `tail` pointer. | `O(1)` |
| `addAtPosition(position, element)` | Inserts a new node at a specific 1-indexed position. | `O(n)` |
| `removeFirst()` | Removes and returns the element at the head of the list. | `O(1)` |
| `removeLast()` | Removes and returns the element at the tail of the list. | `O(n)` |
| `removeAtPosition(position)` | Removes and returns the element at a specific 1-indexed position. | `O(n)` |

---

##  Architectural Highlights

* **Tail Optimization for Insertions (`O(1)`):** By maintaining an explicit reference to `self.tail`, appending nodes with `addLast()` bypasses full list traversal, bringing time complexity down from `O(n)` to `O(1)`.
* **The Singly Linked Trade-off (`removeLast` is `O(n)`):** Even with a `tail` pointer, removing the tail node still requires `O(n)` time. Because nodes only store a forward `next` reference, updating `self.tail` requires traversing from `self.head` to locate the second-to-last node.

---

##  Usage Example

```python
from singly_linked_list import SinglyLinkedList

# Initialize the list
my_list = SinglyLinkedList()

# Insert elements
my_list.addFirst(10)          # List: 10
my_list.addLast(30)           # List: 10->30
my_list.addAtPosition(2, 20)  # List: 10->20->30

print(my_list)                # Output: 10->20->30
print(len(my_list))           # Output: 3

# Remove elements
val1 = my_list.removeFirst()       # Returns 10, List: 20->30
val2 = my_list.removeAtPosition(1)   # Returns 20, List: 30
val3 = my_list.removeLast()         # Returns 30, List: Empty list

print(my_list)                # Output: Empty list
print(len(my_list))           # Output: 0