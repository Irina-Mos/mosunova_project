def square(length: int, symbol: str, val: bool):
    """
    Функция, которая отображает пустой или заполненный квадрат из некоторого символа.
    :param length: Длина стороны квадрата.
    :param symbol: Символ.
    :param val: Пустой (False) или заполненый (True) квадрат.
    """
    if val:
        for i in range(0, length):
            for j in range(0, length):
                print(symbol, end=" ")
            print('\n', end="")
    elif val == False:
        for j in range(0, length):
            print(symbol, end=" ")
        print('\n', end="")
        for i in range(1, length - 1):
            print(symbol, end=" ")
            for j in range(1, length - 1):
                print(" ", end=" ")
            print(symbol)
        for j in range(0, length):
            print(symbol, end=" ")
    else:
        print('Invalid input')

square(7, "$", True)
print('\n')
square(7, "$", False)