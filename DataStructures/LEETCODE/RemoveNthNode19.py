from typing import Optional, Tuple


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def removeNthFromEnd(self, head, n):
        newList = ListNode(head.val, head.next)
        previousNode = newList
        currentNode = newList
        nextNode = currentNode.next
        while nextNode is not None:
            if n == 0:
                if nextNode.next is None:
                    previousNode.next = None
                    currentNode.next = None

                else:
                    tmp = nextNode.next
                    currentNode.next = tmp
                    nextNode.next = None
                nextNode = None
            else:
                previousNode = currentNode
                currentNode = nextNode
                if nextNode.next is not None:
                    nextNode = currentNode.next

            n -= 1

        if n > 0:
            return None
        else:
            return newList

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
        self.assertEqual(None, assertedValue.val)



