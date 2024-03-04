from typing import Optional, Tuple


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





class Solution(object):
    def find_length(self, head):
        current_value = head
        length = 0
        if head is None:
            return current_value
        current_value = head
        while current_value is not None:
            length += 1
            current_value = current_value.next

        return length
    def removeNthFromEnd(self, head, n):
        length = self.find_length(head)
        numberOfIterations = length - n - 1
        i = 0
        if numberOfIterations == -1:
            return head.next

        current_node = head
        while i < numberOfIterations:
            current_node = current_node.next
            i += 1

        current_node.next = current_node.next.next
        return head


import unittest
class RemoveNthNode19(unittest.TestCase):

    def test_removeNthFromEnd_GivenLinkedListWithOneNodeAndNIsBiggerThanLengthReturnNone(self):
        list = ListNode(1)
        result = Solution().removeNthFromEnd(list,1)

        self.assertEqual(None, result)

    def test_removeNthFromEnd_GivenLinkedListWithTwoNodeAndNIsLessThanLengthReturnNone(self):
        list = ListNode(1, ListNode(2))
        result = Solution().removeNthFromEnd(list, 1)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next, None)

    def test_removeNthFromEnd_GivenBigListAndNIsLessThanLengthOfLinkedListReturnItsHead(self):
        list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = Solution().removeNthFromEnd(list, 2)

        assertedValue = result
        self.assertEqual(1, assertedValue.val)
        assertedValue = assertedValue.next
        self.assertEqual(2, assertedValue.val, )
        assertedValue = assertedValue.next
        self.assertEqual(3, assertedValue.val, )
        assertedValue = assertedValue.next
        self.assertEqual(5, assertedValue.val, )

    def test_removeNthFromEnd_GivenListAndNIsTheSameSizeThanLengthOfListShouldRemoveItsHead(self):
        list = ListNode(1, ListNode(2))
        result = Solution().removeNthFromEnd(list, 2)

        assertedValue = result
        self.assertEqual(2, assertedValue.val)
        assertedValue = assertedValue.next
        self.assertEqual(None, assertedValue)



