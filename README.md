#  Python Data Structures & Algorithms

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

A clean, production-focused repository implementing core data structures and algorithms from first principles in Python. Built with an emphasis on **algorithmic complexity trade-offs**, **memory efficiency**, and **rigorous unit test coverage**.


---

##  Implementation Dashboard

### 1. Data Structures

| Category | Data Structure | Status | Time Complexity (Avg/Worst) | Space | Spec & Docs |
|---|---|:---:|:---:|:---:|:---:|
| **Linked Lists** | Singly Linked List (Tail-Optimized) | Complete | Search: $O(n)$ \| Insert: $O(1)$ \| Delete: $O(n)$ | $O(n)$ | [View Spec](data_structures/linked_lists/singly_linked_list/README.md) |
| | Doubly Linked List | Next | Search: $O(n)$ \| Insert: $O(1)$ \| Delete: $O(1)$ | $O(n)$ | *Planned* |
| **Stacks & Queues** | Array-based / Linked Stack | Planned | Push: $O(1)$ \| Pop: $O(1)$ | $O(n)$ | *Planned* |
| | Queue (FIFO) | Planned | Enqueue: $O(1)$ \| Dequeue: $O(1)$ | $O(n)$ | *Planned* |
| **Hash-based** | Hash Table (Separate Chaining) | Planned | Search: $O(1)$ \| Insert: $O(1)$ | $O(n)$ | *Planned* |
| **Trees** | Binary Search Tree (BST) | Planned | Search: $O(\log n)$ \| Insert: $O(\log n)$ | $O(n)$ | *Planned* |
| **Graphs** | Adjacency List Graph | Planned | Traversal: $O(V + E)$ | $O(V + E)$ | *Planned* |

---

##  Engineering & Algorithmic Highlights

* **Tail Optimization in Singly Linked Lists:** Maintains an explicit `self.tail` pointer alongside `self.head`. This guarantees $O(1)$ constant time execution for `addLast()` operations without requiring an $O(n)$ full traversal.
* **Deterministic Test State:** Built using Python's standard `unittest` framework with automated `setUp` fixtures to eliminate test-state leakage across assertions.
* **Zero External Dependencies:** Implemented purely in standard Python 3.10+ without third-party runtime dependencies.

---

##  Getting Started

### Prerequisites
* Python 3.10 or higher installed.

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/python-data-structures-and-algorithms.git](https://github.com/your-username/python-data-structures-and-algorithms.git)
   cd python-data-structures-and-algorithms
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

---

##  Running Unit Tests

This repository utilizes Python's built-in `unittest` module for test execution and discovery.

* **Run the entire test suite:**
  ```bash
  python -m unittest discover tests
  ```

* **Run a specific test file:**
  ```bash
  python -m unittest tests/test_singly_linked_list.py
  ```

---

##  Author & License

* **Author:** Agosu jubril sonayon
* **License:** Distributed under the MIT License. See `LICENSE` for details.