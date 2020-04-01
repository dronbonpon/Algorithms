from CountSplitInv import count_split_inv

def number_of_inversions(arr:list):
    """
    Функция сортировки списка чисел и поиска инверсий в нем
    :param arr: Список чисел
    :return: Отсортированный список и количество иверсий
    """
    if len(arr) == 0 or len(arr) == 1:
        return arr, 0
    c, left_inv = number_of_inversions(arr[:len(arr)//2])
    d, right_inv = number_of_inversions(arr[len(arr)//2:])
    b, split_inv = count_split_inv(c, d)
    return b, left_inv + right_inv + split_inv
