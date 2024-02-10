class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# class LinkedList:
class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head.value is None:
            self.length = 1
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head.value is None:
            self.length = 1
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1


my_linked_list = LinkedList(4)
my_linked_list.append(5)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1

"""

import unittest

class LinkedListTests(unittest.TestCase):
    def test_init_emptylinked_list(self):
        new_linked_list = LinkedList(None)

        self.assertEqual(new_linked_list.length, 1)
        self.assertEqual(new_linked_list.tail,new_linked_list.head)

    def test_append_emptylinkedlist_thenupdateHeadAndTail(self):
        new_linked_list = LinkedList(None)
        new_linked_list.append(4)
        self.assertEqual(new_linked_list.length, 1)
        self.assertEqual(new_linked_list.tail,new_linked_list.head)

        self.assertEqual(new_linked_list.head.value, 4)
        self.assertEqual(new_linked_list.head.next, None)

        self.assertEqual(new_linked_list.tail.value, 4)
        self.assertEqual(new_linked_list.tail.next, None)

    def test_append_linkedlist_updateHeadAndTailWithNewValue(self):
        new_linked_list = LinkedList(4)
        new_linked_list.append(2)

        self.assertEqual(new_linked_list.length, 2)
        self.assertNotEqual(new_linked_list.tail, new_linked_list.head)

        self.assertEqual(new_linked_list.head.value, 4)
        self.assertEqual(new_linked_list.head.next.value, 2)

        self.assertEqual(new_linked_list.tail.value, 2)
        self.assertEqual(new_linked_list.tail.next, None)

# Pop Tests
    def test_pop_emptyLinkedListReturnsNothing(self):
        new_linked_list = LinkedList(None)
        nodePopped = new_linked_list.pop()

        self.assertEqual(None, nodePopped.value)
        self.assertEqual(None, nodePopped.next)

    def test_pop_emptyLinkedListLengthOfListIs0(self):
        new_linked_list = LinkedList(None)
        new_linked_list.pop()

        self.assertEqual(0, new_linked_list.length)

    def test_pop_LinkedListWithOneNodeReturnsNode(self):
        new_linked_list = LinkedList(4)
        new_linked_list.pop()

        self.assertEqual(0, new_linked_list.length)

    def test_pop_LinkedListWithOneNodeReturnsNode(self):
        new_linked_list = LinkedList(4)
        nodePopped = new_linked_list.pop()

        self.assertEqual(4, nodePopped.value)
        self.assertEqual(None, nodePopped.next)

    def test_pop_LinkedListWithMultipleNodesUpdatesTailAndLastNode(self):
        new_linked_list = LinkedList(4)
        new_linked_list.append(10)
        new_linked_list.append(122)
        new_linked_list.append(22)

        self.assertEqual(22, new_linked_list.tail.value)
        self.assertEqual(None, new_linked_list.tail.next)
        new_linked_list.pop()

        self.assertEqual(122, new_linked_list.tail.value)
        self.assertEqual(None, new_linked_list.tail.next)

 # Pepend Tests
    def test_prepend_LinkedListWithNoNodesPrependNode(self):
        new_linked_list = LinkedList(None)

        new_linked_list.prepend(4)

        self.assertEqual(new_linked_list.head.value, 4)
        self.assertEqual(new_linked_list.tail.value, 4)

    def test_prepend_NonEmptyLinkedListUpdatesHeadWithNewNode(self):
        new_linked_list = LinkedList(4)
        new_linked_list.append(10)
        new_linked_list.append(122)
        new_linked_list.append(22)

        self.assertEqual(new_linked_list.head.value, 4)

        new_linked_list.prepend(100)

        self.assertEqual(new_linked_list.head.value, 100)
        self.assertEqual(new_linked_list.head.next.value, 4)
        self.assertEqual(new_linked_list.length, 5)

if __name__ == '__main__':
    unittest.main()