def binary_search(arr, x):
    """
    Реализация рекурсивного бинарного поиска
    :param arr: Список чисел, в котором производится поиск
    :param x: Искомое число
    :return: True, если такое число есть. False, если его нет
    """
    if len(arr) == 1:
        return True if arr[0] == x else False
    if arr[len(arr)//2] == x:
        return True
    if arr[len(arr)//2] < x:
        return binary_search(arr[len(arr)//2:], x)
    if arr[len(arr)//2] > x:
        return binary_search(arr[:len(arr) // 2], x)
    return False
