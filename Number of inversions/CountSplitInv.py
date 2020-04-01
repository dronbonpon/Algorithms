def count_split_inv(c, d):
    """
    Считает количество иверсий между левой и правой частью списка
    :param c: Левая часть списка
    :param d: Правая часть списка
    :return: Отсортированный массив и число разделенных иверсий
    """
    b = [0]*(len(c) + len(d))
    i, j, split_inv = 0, 0, 0
    k = 0
    while i < len(c) and j < len(d):
        if c[i] > d[j]:
            b[k] = d[j]
            j += 1
            #(len(b)//2) - i - Оставшееся количество в С
            split_inv += (len(b)//2) - i
        else:
            b[k] = c[i]
            i += 1
        k += 1
    while i < len(c):
        b[k] = c[i]
        i += 1
        k += 1
    while j < len(d):
        b[k] = d[j]
        j += 1
        k += 1
    return b, split_inv

