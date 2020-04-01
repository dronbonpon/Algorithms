import unittest
from Is_two_elements import is_two_elements


class Test_is_two_elements(unittest.TestCase):
    """
    Тестовый модуль
    """
    def test_1(self):
        self.assertTrue(is_two_elements([3, 7, 4, 2], 5))

    def test_2(self):
        self.assertFalse(is_two_elements([7, 7, 9, 8, 1], 7))

    def test_3(self):
        self.assertFalse(is_two_elements([3, 5, 7, 2, 0, 2], 6))

    def test_4(self):
        self.assertTrue(is_two_elements([0, 0, 1], 1))


if __name__ == '__main__':
    unittest.main()
