import unittest

from main import suma, resta


class TestSuma(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(4, suma(3, 1))

    def test_resta(self):
        self.assertEqual(1, resta(3, 2))


if __name__ == '__main__':
    unittest.main()
