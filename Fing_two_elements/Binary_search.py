def binary_search(arr, x, y):
    """
    Реализация рекурсивного бинарного поиска
    :param arr: Список чисел, в котором производится поиск
    :param x: Искомое число
    :return: True, если такое число есть. False, если его нет
    """
    mid = len(arr) // 2
    low = 0
    high = len(arr) - 1

    while arr[mid] != x and low <= high:
        if x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    return False if low > high or mid == y else True


