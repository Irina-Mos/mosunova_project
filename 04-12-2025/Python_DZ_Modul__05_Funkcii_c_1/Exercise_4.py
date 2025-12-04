def min_num(num_1: int, num_2: int, num_3: int, num_4: int, num_5: int) -> int:
    """
    Функция, которая возвращает минимальное из пяти чисел.
    :param num_1: Число 1.
    :param num_2: Число 2.
    :param num_3: Число 3.
    :param num_4: Число 4.
    :param num_5: Число 5.
    :return: Минимальное из 5 введенных чисел.
    """
    num_list = []
    num_list.append(num_1)
    num_list.append(num_2)
    num_list.append(num_3)
    num_list.append(num_4)
    num_list.append(num_5)
    num_min = min(num_list)
    return num_min

x = min_num(2, 30, 60, 1, 9)
print(x)