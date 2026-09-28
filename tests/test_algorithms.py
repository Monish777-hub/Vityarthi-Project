import unittest
from modules.algorithms import gcd, factorial, fibonacci, is_prime, prime_factors
from modules.array_tools import reverse_array, find_max, remove_duplicates, kth_smallest
from modules.search_sort import linear_search, binary_search, bubble_sort


class TestAlgoLabs(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), [0, 1, 1, 2, 3, 5])

    def test_prime(self):
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(30))

    def test_prime_factors(self):
        self.assertEqual(prime_factors(84), [2, 2, 3, 7])

    def test_array_tools(self):
        self.assertEqual(reverse_array([1, 2, 3]), [3, 2, 1])
        self.assertEqual(find_max([4, 9, 2]), 9)
        self.assertEqual(remove_duplicates([1, 2, 1, 3]), [1, 2, 3])
        self.assertEqual(kth_smallest([7, 2, 5], 2), 5)

    def test_search_sort(self):
        self.assertEqual(linear_search([5, 8, 2], 8), 1)
        self.assertEqual(binary_search([2, 5, 8], 5), 1)
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
