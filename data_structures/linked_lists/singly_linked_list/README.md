# Singly Linked List in Python

A clean, efficient implementation of a **Singly Linked List** built from scratch in Python. 

Unlike standard singly linked lists that only track the head, this implementation maintains both **`head`** and **`tail`** pointers, enabling optimized **`O(1)` constant-time insertion** at the tail.

---

##  Features & Implemented Methods

| Method | Description | Time Complexity |
|---|---|---|
| `__init__()` | Initializes an empty list with head = None, tail = None, and size = 0. | `O(1)` |
| `__len__()` | Returns the current number of elements using Python's built-in len() function. | `O(1)` |
| `__str__()` | Provides a visual string representation of the list (e.g., 10->20->30). | `O(n)` |
| `addFirst(element)` | Adds a new node to the very beginning of the list. | `O(1)` |
| `addLast(element)` | Adds a new node to the end of the list using the tail pointer. | `O(1)` |
| `addAtPosition(position, element)` | Inserts a new node at a specific 1-indexed position. | `O(n)` |

##  Key Architectural Choice: Tail Optimization

Normally, adding an element to the tail of a standard singly linked list requires a traversal from the head, resulting in `O(n)` time complexity. 

By tracking `self.tail`, our `addLast` method directly accesses the end of the list, bypassing the need for a loop and reducing the operation down to `O(1)` time complexity.

##  Code Example

```python
from singly_linked_list import SinglyLinkedList

# Initialize the list
my_list = SinglyLinkedList()

# Add items
my_list.addFirst(10)          # List: 10
my_list.addLast(30)           # List: 10->30
my_list.addAtPosition(2, 20)  # List: 10->20->30

# Check length and print
print(len(my_list))   # Output: 3
print(my_list)        # Output: 10->20->30