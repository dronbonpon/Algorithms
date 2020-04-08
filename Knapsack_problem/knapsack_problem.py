def relative_sort(cost, weight):
    """
    Сортирует массив стоимостей и весов предметов по убыванию отношения стоимости предмета
    к его весу
    :param cost: Массив стоимостей предметов
    :param weight: Массив весов предметов
    :return: Отсортированные массивы стоимостей и весов предметов
    """
    result = cost
    if len(cost) > 1:
        mid = len(cost) // 2
        left_cost, left_weight = relative_sort(cost[:mid], weight[:mid])
        right_cost, right_weight = relative_sort(cost[mid:], weight[mid:])
        i = j = k = 0
        while i < len(left_cost) and j < len(right_cost):
            if left_cost[i] / left_weight[i] > right_cost[j] / right_weight[j]:
                result[k] = left_cost[i]
                weight[k] = left_weight[i]
                i += 1
            else:
                result[k] = right_cost[j]
                weight[k] = right_weight[j]
                j += 1
            k += 1
        while i < len(left_cost):
            result[k] = left_cost[i]
            weight[k] = left_weight[i]
            i += 1
            k += 1
        while j < len(right_cost):
            result[k] = right_cost[j]
            weight[k] = right_weight[j]
            j += 1
            k += 1
    return result, weight


def backpack_problem(cost, weight, w):
    """
    Основная программа решения задачи
    :param cost: Массив стоимостей
    :param weight: Массив весов
    :param w: Вместимость рюкзака
    :return: Максимальная стоимость 
    """
    cost, weight = relative_sort(cost, weight)
    result = 0
    i = 0
    while i < len(cost) and w > 0:
        if w >= weight[i]:
            result += cost[i]
            w -= weight[i]
        else:
            result += (w/weight[i]) * cost[i]
            w = 0
        i += 1
    return f"{result:.3f}"


def main():
    n, w = list(map(int, input().split()))
    weight = []
    cost = []
    for j in range(n):
        tmp = list(map(int, input().split()))
        cost.append(tmp[0])
        weight.append(tmp[1])

    result = backpack_problem(cost, weight, w)
    print(result)


if __name__ == '__main__':
    main()