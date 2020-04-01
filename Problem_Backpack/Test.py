import unittest
from Problem_Backpack import problem_backpack


class Test_problem_backpack(unittest.TestCase):
    """
    Тестовый модуль
    """

    def test_1(self):
        self.assertEqual(problem_backpack([8, 15], [1, 8], 9), 23)

    def test_2(self):
        self.assertEqual(problem_backpack([7, 15, 7, 6, 7, 3],
                                          [5, 8, 15, 11, 10, 26], 29), 29)

    def test_3(self):
        self.assertEqual((problem_backpack([17, 15, 6, 3, 29],
                                           [15, 15, 1, 1, 23], 40)), 55)


if __name__ == '__main__':
    unittest.main()
