def problem_backpack(values, weights, w):
    """
    Реалтзация алгоритма решения дискретной проблемы рюкзака
    посредством динамического программирования
    :param values: 'Цены' предметов
    :param weights: 'Веса' предметов
    :param w: 'Вместимость' портфеля
    :return: Максимальная ценность предметов, которые поместятся в рюкзаке
    """
    #Cоздаем матрицу, инициализируем ее нулями
    m = [[0] * (w+1) for i in range(len(values)+1)]

    for i in range(1, len(values)+1):
        for j in range(w+1):
            #Если вес текущего предмета больше
            #текущей вместимости рюкзака, игнорируем этот предмет
            if weights[i-1] > j:
                m[i][j] = m[i-1][j]
            #В противном случае у нас есть два пути. Первый -
            # - проигнорировать текущий предмет и пойти дальше.
            #Второй - попробовать уместить текущий предмет в рюкзак
            #Выбирается наилучший путь
            else:
                m[i][j] = max(m[i-1][j], m[i-1][j-weights[i-1]]+values[i-1])
    return m[len(values)][w]



