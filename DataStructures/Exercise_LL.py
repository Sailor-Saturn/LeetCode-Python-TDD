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

    def set(self, index, new_value):
        tmp = self.get(index)
        if tmp is not None:
            tmp.value = new_value

    def insert(self, index, new_value):
        if index == 0 :
            self.prepend(new_value)
        elif index == self.length:
            self.append(new_value)
        elif index > 0 and index <= self.length:
            tmp = self.get(index-1)
            new_node = Node(new_value)
            new_node.next = tmp.next
            tmp.next = new_node
            self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.popFirst()
        elif index == self.length - 1:
            return self.pop()
        elif 0 < index <= self.length:
            previous_node = self.get(index - 1)
            node_to_be_removed = previous_node.next
            next_node = node_to_be_removed.next
            previous_node.next = next_node

            node_to_be_removed.next = None
            self.length -= 1
            return node_to_be_removed



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


def create_linked_list_with_items():
    new_linked_list = LinkedList(4)
    new_linked_list.append(10)
    new_linked_list.append(122)
    new_linked_list.append(22)
    return new_linked_list


class LinkedListTests(unittest.TestCase):
    def test_init_emptylinked_list(self):
        new_linked_list = LinkedList(None)

        self.assertEqual(new_linked_list.tail,new_linked_list.head)

    def test_init_LinkedListWithNoneNodeLengthIsZero(self):
        new_linked_list = LinkedList(None)

        self.assertEqual(new_linked_list.length, 0)

    def test_append_emptylinkedlist_thenupdateHeadAndTail(self):
        new_linked_list = self.create_empty_linked_list()
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
        new_linked_list = self.create_empty_linked_list()
        nodePopped = new_linked_list.pop()

        self.assertEqual(None, None)

    def test_pop_emptyLinkedListLengthOfListIs0(self):
        new_linked_list = self.create_empty_linked_list()
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
        new_linked_list = create_linked_list_with_items()

        self.assertEqual(22, new_linked_list.tail.value)
        self.assertEqual(None, new_linked_list.tail.next)
        new_linked_list.pop()

        self.assertEqual(122, new_linked_list.tail.value)
        self.assertEqual(None, new_linked_list.tail.next)

    # Pre pend Tests
    def test_prepend_LinkedListWithNoNodesPrependNode(self):
        new_linked_list = self.create_empty_linked_list()

        new_linked_list.prepend(4)

        self.assertEqual(new_linked_list.head.value, 4)
        self.assertEqual(new_linked_list.tail.value, 4)

    def test_prepend_NonEmptyLinkedListUpdatesHeadWithNewNode(self):
        new_linked_list = create_linked_list_with_items()

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
        new_linked_list = self.create_empty_linked_list()
        self.assertEqual(new_linked_list.head.value, None)
        self.assertEqual(new_linked_list.tail.value, None)

        popFirstNode = new_linked_list.popFirst()
        self.assertEqual(new_linked_list.head.value, None)
        self.assertEqual(new_linked_list.tail.value, None)

        self.assertEqual(popFirstNode, None)
        self.assertEqual(new_linked_list.length, 0)

    def test_popFirst_NonEmptyLinkedListShouldReturnFirstNode(self):
        new_linked_list = create_linked_list_with_items()

        popFirstNode = new_linked_list.popFirst()

        self.assertEqual(new_linked_list.head.value, 10)
        self.assertEqual(new_linked_list.head.next.value, 122)

        self.assertEqual(popFirstNode.value, 4)
        self.assertEqual(new_linked_list.length, 3)

    def test_popFirst_NonEmptyListPoppedNodeShouldNotReferenceLinkedList(self):
        new_linked_list = create_linked_list_with_items()

        popFirstNode = new_linked_list.popFirst()

        self.assertEqual(popFirstNode.value, 4)
        self.assertEqual(popFirstNode.next, None)

    # Get Tests
    def test_get_EmptyLinkedListShouldReturnNone(self):
        new_linked_list = self.create_empty_linked_list()

        getNode = new_linked_list.get(0)

        self.assertEqual(getNode, None)

    def test_get_IndexOutOfBoundsEmptyLinkedListShouldReturnNone(self):
        new_linked_list = self.create_empty_linked_list()

        getNode = new_linked_list.get(100)

        self.assertEqual(getNode, None)

    def test_get_NonEmptyLinkedlistShouldReturnNone(self):
        new_linked_list = create_linked_list_with_items()

        getNode = new_linked_list.get(2)

        self.assertEqual(getNode.value, 122)
        self.assertEqual(getNode.next.value, 22)

    def test_set_IndexOutOfBoundsLinkedListShouldNotChangeAnything(self):
        new_linked_list = create_linked_list_with_items()

        expected_linked_list = create_linked_list_with_items()

        new_linked_list.set(10, 15000)

        self.checkIfTwoLinkedListsAreEqual(expected_linked_list, new_linked_list)

    def test_set_NonEmptyLinkedListWithValidIndexShouldSubstituteValue(self):
        new_linked_list = create_linked_list_with_items()

        new_linked_list.set(2, 1500)

        self.assertEqual(new_linked_list.get(2).value, 1500)

    # Insert Tests
    def test_insert_AtIndexZero_OnEmptyLinkedList_ShouldInsertElement(self):
        new_linked_list = self.create_empty_linked_list()

        new_linked_list.insert(0, 1)

        self.assertEqual(new_linked_list.head.value, 1)

    def test_insert_NotFirstIndex_OnEmptyLinkedList_ShouldNotInsertElement(self):
        new_linked_list = self.create_empty_linked_list()

        new_linked_list.insert(1, 1)

        self.assertEqual(new_linked_list.get(1), None)

    def test_insert_NotFirstIndex_OnNonEmptyLinkedList_ShouldInsertElement(self):
        new_linked_list = LinkedList(5)

        new_linked_list.insert(1, 1)

        self.assertEqual(new_linked_list.get(1).value, 1)

    def test_insert_FirstIndex_OnNonEmptyLinkedList_ShouldInsertElement(self):
        new_linked_list = LinkedList(5)

        new_linked_list.insert(0, 1)

        self.assertEqual(new_linked_list.get(0).value, 1)
        self.assertEqual(new_linked_list.get(0).next.value, 5)

    def test_insert_AtNegativeIndex_OnEmptyLinkedList_ShouldNotInsertElement(self):
        new_linked_list = self.create_empty_linked_list()

        new_linked_list.insert(-1, 1)

        self.assertEqual(new_linked_list.get(-1), None)


    def test_remove_AtNegativeIndex_OnEmptyLinkedList_ShouldNotRemoveElement(self):
        new_linked_list = self.create_empty_linked_list()

        self.assertEqual(new_linked_list.length, 0)

        new_linked_list.remove(-1)

        self.assertEqual(new_linked_list.length, 0)

    def test_remove_AtNegativeIndex_OnLinkedListWithItems_ShouldNotRemoveElement(self):
        new_linked_list = create_linked_list_with_items()

        self.assertEqual(new_linked_list.length, 4)

        new_linked_list.remove(-1)

        self.assertEqual(new_linked_list.length, 4)

    def test_remove_AtIndexBiggerThanLength_OnLinkedListWithItems_ShouldNotRemoveElement(self):
        new_linked_list = create_linked_list_with_items()

        self.assertEqual(new_linked_list.length, 4)

        new_linked_list.remove(5)

        self.assertEqual(new_linked_list.length, 4)

    def test_remove_AtIndex_OnLinkedListWithItems_ShouldRemoveElement(self):
        new_linked_list = create_linked_list_with_items()

        self.assertEqual(new_linked_list.length, 4)

        removedNode = new_linked_list.remove(1)

        self.assertEqual(new_linked_list.length, 3)
        self.assertEqual(removedNode.value, 10)

    def test_remove_AtFirstIndex_OnLinkedListWithItems_ShouldRemoveElement(self):
        new_linked_list = create_linked_list_with_items()

        self.assertEqual(new_linked_list.length, 4)

        removedNode = new_linked_list.remove(0)

        self.assertEqual(new_linked_list.length, 3)
        self.assertEqual(removedNode.value, 4)

    def test_remove_AtLastIndex_OnLinkedListWithItems_ShouldRemoveElement(self):
        new_linked_list = create_linked_list_with_items()

        self.assertEqual(new_linked_list.length, 4)

        removedNode = new_linked_list.remove(3)

        self.assertEqual(new_linked_list.length, 3)
        self.assertEqual(removedNode.value, 22)

    # Helpers

    def create_empty_linked_list(self):
        return LinkedList(None)

    def checkIfTwoLinkedListsAreEqual(self, expected_linked_list, received_linked_list):
        expected_node = expected_linked_list.head
        received_node = received_linked_list.head

        while expected_node is not None and received_node is not None:
            self.assertEqual(expected_node.value, received_node.value,
                             "Check if the node is identical for the same index")

            expected_node = expected_node.next
            received_node = received_node.next

if __name__ == '__main__':
    unittest.main()