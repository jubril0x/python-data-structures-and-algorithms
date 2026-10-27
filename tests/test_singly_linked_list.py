import unittest
from data_structures.linked_lists.singly_linked_list.singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        """
        This setUp method runs automatically before every single test method.
        This makes sure each test starts with an empty linked list.
        """
        self.sll = SinglyLinkedList()

    def test_initialization(self):
        """Testing that a newly created list is empty"""
        self.assertIsNone(self.sll.head)
        self.assertIsNone(self.sll.tail)
        self.assertEqual(len(self.sll), 0)
        self.assertEqual(str(self.sll), "Empty list")


    def test_add_first(self):
        """Testing inserting elements at the beginning of the list"""
        self.sll.addFirst(10)
        self.assertEqual(self.sll.head.element, 10)
        self.assertEqual(self.sll.tail.element, 10)
        self.assertEqual(len(self.sll), 1)

        self.sll.addFirst(5)
        self.assertEqual(self.sll.head.element, 5)
        self.assertEqual(self.sll.tail.element, 10)
        self.assertEqual(len(self.sll), 2)
        self.assertEqual(str(self.sll), "5->10")

    def test_add_last(self):
        """Testing appending elements to the end of the list"""
        self.sll.addLast(10)
        self.assertEqual(self.sll.head.element, 10)
        self.assertEqual(self.sll.tail.element, 10)

        self.sll.addLast(20)
        self.assertEqual(self.sll.head.element, 10)
        self.assertEqual(self.sll.tail.element, 20)
        self.assertEqual(len(self.sll), 2)
        self.assertEqual(str(self.sll), "10->20")

    def test_add_at_position(self):
        """Testing inserting elements at specific positions"""
        self.sll.addLast(10)
        self.sll.addLast(30)

        # Inserting at middle position
        self.sll.addAtPosition(2, 20)
        self.assertEqual(str(self.sll), "10->20->30")
        self.assertEqual(len(self.sll), 3)

        # Inserting at position 1 (head) using addAtPosition
        self.sll.addAtPosition(1, 5)
        self.assertEqual(str(self.sll), "5->10->20->30")

    def test_add_at_position_invalid(self):
        """Testing that invalid insertion positions raise an IndexError."""
        with self.assertRaises(IndexError):
            self.sll.addAtPosition(0, 72)

        with self.assertRaises(IndexError):
            self.sll.addAtPosition(5, 65)


    def test_remove_first(self):
        """Testing removing elements from the front of the list"""
        self.sll.addLast(10)
        self.sll.addLast(20)

        removed = self.sll.removeFirst()
        self.assertEqual(removed, 10)
        self.assertEqual(self.sll.head.element, 20)
        self.assertEqual(len(self.sll), 1)

        # Removing last remaining element
        removed_last = self.sll.removeFirst()
        self.assertEqual(removed_last, 20)
        self.assertIsNone(self.sll.head)
        self.assertIsNone(self.sll.tail)
        self.assertEqual(len(self.sll), 0)

    def test_remove_last(self):
        """Testing removing elements from the end of the list"""
        self.sll.addLast(10)
        self.sll.addLast(20)

        removed = self.sll.removeLast()
        self.assertEqual(removed, 20)
        self.assertEqual(self.sll.tail.element, 10)
        self.assertEqual(len(self.sll), 1)

        # Removing last remaining element
        removed_last = self.sll.removeLast()
        self.assertEqual(removed_last, 10)
        self.assertIsNone(self.sll.head)
        self.assertIsNone(self.sll.tail)
        self.assertEqual(len(self.sll), 0)

    def test_remove_at_position(self):
        """Testing removing elements from specific positions"""
        self.sll.addLast(10)
        self.sll.addLast(20)
        self.sll.addLast(30)

        # Removing the middle element
        removed = self.sll.removeAtPosition(2)
        self.assertEqual(removed, 20)
        self.assertEqual(str(self.sll), "10->30")
        self.assertEqual(len(self.sll), 2)

    def test_remove_from_empty_list(self):
        """Testing that removing from an empty list raises an IndexError"""
        with self.assertRaises(IndexError):
            self.sll.removeFirst()

        with self.assertRaises(IndexError):
            self.sll.removeLast()

    def test_remove_at_position_invalid(self):
        """Testing that invalid removal positions raise an IndexError"""
        self.sll.addLast(10)
        with self.assertRaises(IndexError):
            self.sll.removeAtPosition(0)

        with self.assertRaises(IndexError):
            self.sll.removeAtPosition(5)


if __name__ == "__main__":
    unittest.main()