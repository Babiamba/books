from unittest import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 12, '+')
        self.assertEqual(18, result)

    def test_minus(self):
        result = operations(3, 4, '-')
        self.assertEqual(-1, result)

    def test_multiply(self):
        result = operations(6, 12, '*')
        self.assertEqual(72, result)

    def test_div(self):
        result = operations(12, 1, '/')
        self.assertEqual(12, result)
