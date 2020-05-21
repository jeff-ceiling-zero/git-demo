import unittest
import fizzbuzz

# TDD
# 1. WRite a test, that FAILS
# 2. Fix the test with the MINIMUM amount of code to get it passing
# 3. goto to #1


class MyTestCase(unittest.TestCase):

    def test_num_to_string(self):
        self.assertEqual('1', fizzbuzz.num_to_fizz_string(1))
        self.assertEqual('2', fizzbuzz.num_to_fizz_string(2))
        self.assertEqual('Fizz', fizzbuzz.num_to_fizz_string(3))
        self.assertEqual('4', fizzbuzz.num_to_fizz_string(4))
        self.assertEqual('Buzz', fizzbuzz.num_to_fizz_string(5))
        self.assertEqual('FizzBuzz', fizzbuzz.num_to_fizz_string(15))

    def test_generate_list_of_numbers(self):
        list_of_nums = fizzbuzz.generate_list_of_numbers()
        self.assertEqual(99, len(list_of_nums))
        self.assertEqual(1, list_of_nums[0])
        self.assertEqual(99, list_of_nums[98])


if __name__ == '__main__':
    unittest.main()
