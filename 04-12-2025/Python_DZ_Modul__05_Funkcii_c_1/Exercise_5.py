def product_num(a: int, b: int) -> int:
    """
    Функция, которая возвращает произведение чисел в указанном диапазоне.
    :param a: Нижняя граница диапазона.
    :param b: Верхняя граница диапазона.
    :return: Произведение чисел в указанном диапазоне.
    """
    total = 1
    if a < b:
        for i in range(a, b + 1):
            total *= i
    else:
        for i in range(b, a + 1):
            total *= i
    return total

x = product_num(6, 1)
print(x)