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

        if value is None:
            self.length = 0
        else:
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

    def popFirst(self):

        if self.length == 0:
            self.length = 0
            return None
        else:
            poppedNode = self.head
            if self.head.next is None:

                self.tail = poppedNode.next

            poppedNode = self.head

            self.head = self.head.next
            poppedNode.next = None

            self.length -= 1

            return poppedNode

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next

            return temp


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

        self.assertEqual(new_linked_list.tail,new_linked_list.head)

    def test_init_LinkedListWithNoneNodeLengthIsZero(self):
        new_linked_list = LinkedList(None)

        self.assertEqual(new_linked_list.length, 0)

    def test_append_emptylinkedlist_thenupdateHeadAndTail(self):
        new_linked_list = self.createEmptyLinkedList()
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
        new_linked_list = self.createEmptyLinkedList()
        nodePopped = new_linked_list.pop()

        self.assertEqual(None, None)

    def test_pop_emptyLinkedListLengthOfListIs0(self):
        new_linked_list = self.createEmptyLinkedList()
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
        new_linked_list = self.createLinkedListWithItems()

        self.assertEqual(22, new_linked_list.tail.value)
        self.assertEqual(None, new_linked_list.tail.next)
        new_linked_list.pop()

        self.assertEqual(122, new_linked_list.tail.value)
        self.assertEqual(None, new_linked_list.tail.next)

 # Pepend Tests
    def test_prepend_LinkedListWithNoNodesPrependNode(self):
        new_linked_list = self.createEmptyLinkedList()

        new_linked_list.prepend(4)

        self.assertEqual(new_linked_list.head.value, 4)
        self.assertEqual(new_linked_list.tail.value, 4)

    def test_prepend_NonEmptyLinkedListUpdatesHeadWithNewNode(self):
        new_linked_list = self.createLinkedListWithItems()

        self.assertEqual(new_linked_list.head.value, 4)

        new_linked_list.prepend(100)

        self.assertEqual(new_linked_list.head.value, 100)
        self.assertEqual(new_linked_list.head.next.value, 4)
        self.assertEqual(new_linked_list.length, 5)

    # Pop First
    def test_popFirst_OneItemOnLinkedListShouldReturnThatNodeAndListShouldBeEmpty(self):
        new_linked_list = LinkedList(4)

        popFirstNode = new_linked_list.popFirst()
        self.assertEqual(new_linked_list.head, None)
        self.assertEqual(new_linked_list.tail, None)

        self.assertEqual(popFirstNode.value, 4)
        self.assertEqual(new_linked_list.length, 0)

    def test_popFirst_NoItemsOnLinkedListShouldReturnNone(self):
        new_linked_list = self.createEmptyLinkedList()
        self.assertEqual(new_linked_list.head.value, None)
        self.assertEqual(new_linked_list.tail.value, None)

        popFirstNode = new_linked_list.popFirst()
        self.assertEqual(new_linked_list.head.value, None)
        self.assertEqual(new_linked_list.tail.value, None)

        self.assertEqual(popFirstNode, None)
        self.assertEqual(new_linked_list.length, 0)

    def test_popFirst_NonEmptyLinkedListShouldReturnFirstNode(self):
        new_linked_list = self.createLinkedListWithItems()

        popFirstNode = new_linked_list.popFirst()

        self.assertEqual(new_linked_list.head.value, 10)
        self.assertEqual(new_linked_list.head.next.value, 122)

        self.assertEqual(popFirstNode.value, 4)
        self.assertEqual(new_linked_list.length, 3)

    def test_popFirst_NonEmptyListPoppedNodeShouldNotReferenceLinkedList(self):
        new_linked_list = self.createLinkedListWithItems()

        popFirstNode = new_linked_list.popFirst()

        self.assertEqual(popFirstNode.value, 4)
        self.assertEqual(popFirstNode.next, None)

    # Get Tests
    def test_get_EmptyLinkedListShouldReturnNone(self):
        new_linked_list = self.createEmptyLinkedList()

        getNode = new_linked_list.get(0)

        self.assertEqual(getNode, None)

    def test_get_IndexOutOfBoundsEmptyLinkedListShouldReturnNone(self):
        new_linked_list = self.createEmptyLinkedList()

        getNode = new_linked_list.get(100)

        self.assertEqual(getNode, None)

    def test_get_NonEmptyLinkedlistShouldReturnNone(self):
        new_linked_list = self.createLinkedListWithItems()

        getNode = new_linked_list.get(2)

        self.assertEqual(getNode.value, 122)
        self.assertEqual(getNode.next.value, 22)

    # Helpers
    def createLinkedListWithItems(self):
        new_linked_list = LinkedList(4)
        new_linked_list.append(10)
        new_linked_list.append(122)
        new_linked_list.append(22)
        return new_linked_list

    def createEmptyLinkedList(self):
        return LinkedList(None)

if __name__ == '__main__':
    unittest.main()