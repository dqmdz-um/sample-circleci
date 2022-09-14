import unittest

from main import suma


class TestSuma(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(4, suma(3, 2))


if __name__ == '__main__':
    unittest.main()
