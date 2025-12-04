def palindrome(number: int) -> bool:
    """
    Функция, которая проверяет является ли число палиндромом.
    :param number: Заданное число.
    """
    number_str = str(number)
    pal = True
    for i in range(1, len(number_str) // 2 + 1):
        if number_str[i - 1] == number_str[-i]:
            pass
        else:
            pal = False
            return pal
    return pal

x = palindrome(166151251661)
print(x)
