from MergeSort import merge_sort
from Binary_search import binary_search

def find_two_elements(s, x):
    """
    Проверяет, есть ли в массиве чисел два числа, сумма которых равна x
    :param s: Список чисел
    :param x: Заданное число
    :return: True, если такие два числа есть. False, если их нет
    """
    s = merge_sort(s)
    for y in s:
        if binary_search(s, x-y):
            return True
    return False

