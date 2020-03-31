def merge_sort(arr):
    """
    Функция сортировки списка чисел
    :param arr: Список чисел
    :return: Отсортированный список
    """
    if len(arr) == 1 or len(arr) == 0:
        return arr
    if len(arr) > 1:
        mid = len(arr) // 2

        left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr
