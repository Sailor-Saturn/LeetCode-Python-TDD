class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum

        return nums

import unittest
class RunningSumTests(unittest.TestCase):
        def test_runningSum_ArrayWithOneElementShouldReturnItself(self):
            solution = Solution()
            result = solution.runningSum([1])

            self.assertEqual(result, [1])

        def test_runningSum_ArrayWithTwoElementsShouldReturnTheListOfSumElements(self):
            solution = Solution()
            result = solution.runningSum([1, 2])

            self.assertEqual(result, [1, 3])

        def test_runningSum_ArrayWithTheSameValueRepeatedMultipleTimesShouldReturnSumOfElements(self):
            solution = Solution()
            result = solution.runningSum([1,1,1,1,1])

            self.assertEqual(result, [1,2,3,4,5])

        def test_runningSum_ArrayWithDifferentValuesShouldReturnSumOfElements(self):
            solution = Solution()
            result = solution.runningSum([3,1,2,10,1])

            self.assertEqual(result, [3,4,6,16,17])

        def test_runningSum_emptyArrayShouldReturnItself(self):
            solution = Solution()
            result = solution.runningSum([])

            self.assertEqual(result, [])