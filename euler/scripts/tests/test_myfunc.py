import unittest


from scripts.myfunc import (
    fib, prime_factor, is_prime, primes_below, element_product,
    greatest_product, divisors, sign, lst2num, num2lst, collatz_sequence,
    longest_collatz_sequence
)


class TestMyFunc(unittest.TestCase):
    def test_fib(self):
        test_data = [
            ([1, 2], 3),
            ([3, 12], 15),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(fib(*test_input), test_output)

    def test_prime_factor(self):
        test_data = [
            (6, [2, 3]),
            (1, None),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(prime_factor(test_input), test_output)

    def test_is_prime(self):
        test_data = [
            (2, True),
            (31, True),
            (1, False),
            (1.5, False),
            ('test', False)
        ]
        for test_input, test_output in test_data:
            self.assertEqual(is_prime(test_input), test_output)

    def test_primes_below(self):
        test_data = [
            (6, [2, 3, 5]),
            (2.1, [2]),
            (2, []),
            (11, [2, 3, 5, 7])
        ]
        for test_input, test_output in test_data:
            self.assertEqual(primes_below(test_input), test_output)

    def test_element_product(self):
        test_data = [
            ([1, -2, 3], -6),
            ([0, 1000, 3], 0),
            ([], None)
        ]
        for test_input, test_output in test_data:
            self.assertEqual(element_product(test_input), test_output)

    def test_greatest_product(self):
        test_data = [
            ([[1, 2, 3, 4, 5], 2], 20),
            ([[3, 2, 4, 5], 5], None),
            ([[-1, 2.5, 3, -4, 5], 2], 7.5),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(greatest_product(*test_input), test_output)

    def test_divisors(self):
        test_data = [
            (6, [1, 2, 3, 6]),
            (1.5, []),
            (-2, []),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(divisors(test_input), test_output)

    def test_sign(self):
        test_data = [
            (2, 1),
            (0, 1),
            (-2.6, -1),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(sign(test_input), test_output)

    def test_num2lst(self):
        test_data = [
            (236, [2, 3, 6]),
            (-702, [-7, 0, -2]),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(num2lst(test_input), test_output)

    def test_lst2num(self):
        test_data = [
            ([2, 3, 6], 236),
            ([-7, 0, -2], -702),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(lst2num(test_input), test_output)

    def test_collatz_sequence(self):
        test_data = [
            (4, [4, 2, 1]),
            (13, [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(collatz_sequence(test_input), test_output)        
            
    def test_longest_collatz_sequence(self):
        test_data = [
            (10, 9),
            (100, 97),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(longest_collatz_sequence(test_input), test_output)                