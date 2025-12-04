def count_num(number: int) -> int:
    """
    Функция, которая считает количество цифр в числе.
    :param number: Заданное число.
    :return: Количество цифр в числе.
    """
    counter = 0
    while number != 0:
        number = number // 10
        counter += 1
    return counter

x = count_num(34587)
print(x)

