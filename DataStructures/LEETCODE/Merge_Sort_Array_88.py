import sys


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """


        for i in range(m, m+n):
            nums1[i] = nums2[i-m]

        len = m+n
        for l in range(len - 1):
            for j in range(len - l-1):
                if nums1[j] >= nums1[j + 1]:
                    nums1[j],  nums1[j + 1] = nums1[j + 1], nums1[j]

import unittest
class MergeSortArrayTests(unittest.TestCase):
    def test_merge_FirstArrayHasOneElementAndTheSecondOneHasNoneShouldReturnListWithOnlyFirstElement(self):
        nums1 = [1]
        nums2 = []
        m = 1
        n = 0
        Solution().merge(nums1, m, nums2, n)

        self.assertEqual([1], nums1)

    def test_merge_FirstArrayHasNoElementsAndTheSecondOneHasOneShouldReturnListWithOnlySecondElement(self):
        nums2 = [1]
        nums1 = [0]
        m = 0
        n = 1
        Solution().merge(nums1, m, nums2, n)

        self.assertEqual([1], nums1)

    def test_merge_TwoArraysWithOneElementEachShouldReturnMergedSortedArray(self):
        nums2 = [2]
        nums1 = [1,0]
        m = 1
        n = 1
        Solution().merge(nums1, m, nums2, n)

        self.assertEqual([1,2], nums1)

    def test_merge_TwoArraysWithOneElementEachAndUnsortedShouldReturnSortedArray(self):
        nums2 = [1]
        nums1 = [2,0]
        m = 1
        n = 1
        Solution().merge(nums1, m, nums2, n)

        self.assertEqual([1,2], nums1)

    def test_merge_TwoArraysWithMultipleSortedElementsShouldReturnSortedMergedArray(self):
        nums2 = [2,5,6]
        nums1 = [1,2,3,0,0,0]
        m = 3
        n = 3
        Solution().merge(nums1, m, nums2, n)

        self.assertEqual([1,2,2,3,5,6], nums1)

    def test_merge_TwoArraysWithWithOneOfThemHavingMultipleZeros(self):
        nums2 = [1,2,2]
        nums1 = [-1,0,0,3,3,3,0,0,0]
        m = 6
        n = 3
        Solution().merge(nums1, m, nums2, n)

        self.assertEqual([-1,0,0,1,2,2,3,3,3], nums1)

    def test_merg2e_TwoArraysWithWithOneOfThemHavingMultipleZeros(self):
        nums2 = [1]
        nums1 = [0, 1, 3,3, 0]
        m = 4
        n = 1
        Solution().merge(nums1, m, nums2, n)

        self.assertEqual([0,1, 1 ,3 ,3], nums1)