class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array = []
        i = 1
        while i <= n:
            element_to_append = ''
            if i % 3 == 0:
                element_to_append = "Fizz"
            if i % 5 == 0:
                element_to_append = element_to_append + "Buzz"

            if element_to_append == '':
                array.append(str(i))
            else:
                array.append(element_to_append)

            i += 1
        return  array

import unittest
class FizzBuzzTests(unittest.TestCase):
    def test_fizzBuzz_GivenANumberThatUpToThatNumberIsNotDivisibleBy3or5ShouldReturnAnArrayOfTheNumbersUpToGivenNumber(self):
        result = Solution().fizzBuzz(2)

        self.assertEqual(["1", "2"], result)

    def test_fizzBuzz_GivenANumberThatUpToThatNumberIsDivisibleBy3ShouldReturnAnArrayOfTheNumbersUpToGivenNumber(self):
        result = Solution().fizzBuzz(3)

        self.assertEqual(["1", "2", "Fizz"], result)

    def test_fizzBuzz_GivenANumberThatUpToThatNumberIsDivisibleBy5ShouldReturnAnArrayOfTheNumbersUpToGivenNumber(self):
        result = Solution().fizzBuzz(5)

        self.assertEqual(["1", "2", "Fizz", "4", "Buzz"], result)

    def test_fizzBuzz_GivenANumberThatOneOrMoreOfTheNumbersIsDivisibleBy3And5ShouldReturnFizzBuzz(self):
        result = Solution().fizzBuzz(15)

        self.assertEqual(["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"], result)
