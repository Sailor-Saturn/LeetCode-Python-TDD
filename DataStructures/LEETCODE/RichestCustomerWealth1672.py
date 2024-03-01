class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealth = 0
        for customer in accounts:
            sumi = sum(customer)
            maxWealth = max(maxWealth, sumi)
        return maxWealth


import unittest
class RichestCustomerWealth(unittest.TestCase):
    def test_maximumWealth_sameWealthOnTwoAccountsReturnsTheSameWealth(self):
        solution = Solution()
        result = solution.maximumWealth([[1,2,3],[3,2,1]])

        self.assertEqual(result, 6)

    def test_maximumWealth_wealthIsBiggerInOneAccountThenReturnSumOfWealth(self):
        solution = Solution()
        result = solution.maximumWealth([[1,5],[7,3],[3,5]])

        self.assertEqual(result, 10)