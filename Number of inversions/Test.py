import unittest
from Number_of_inversions import number_of_inversions


class Test_number_of_inversions(unittest.TestCase):
    """
    Тестовый модуль
    """

    def test_count_1(self):
        self.assertEqual(number_of_inversions([1, 2, 3, 4, 5, 6])[1], 0)

    def test_count_2(self):
        self.assertEqual(number_of_inversions([5, 4, 3, 2, 1])[1], 10)

    def test_count_3(self):
        self.assertEqual(number_of_inversions([9, 5, 6, 7, 1, 4, 3, 2, 8])[1], 23)

    def test_sort_1(self):
        self.assertEqual(number_of_inversions([4, 2, 5, 1, 9, 7, 7])[0], [1, 2, 4, 5, 7, 7, 9])

    def test_sort_2(self):
        self.assertEqual(number_of_inversions([9, 5, 6, 7, 1, 4, 3, 2, 8])[0],
                         [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
