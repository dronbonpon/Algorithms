from MergeSort import merge_sort
from Fing_two_elements.Binary_search import binary_search


def is_two_elements(s, x):
    """
    Проверяет, есть ли в массиве чисел два числа, сумма которых равна x
    :param s: Список чисел
    :param x: Заданное число
    :return: True, если такие два числа есть. False, если их нет
    """
    s = merge_sort(s)
    for y in range(len(s)):
        tmp = x - s[y]
        if binary_search(s, tmp, y):
            return True
    return False

print(is_two_elements([3, 7, 5, 7], 14))
