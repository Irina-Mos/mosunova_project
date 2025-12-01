def summ(a, b):
    summa = 0
    if a < b:
        for i in range(a, b + 1):
            summa += i
    else:
        for i in range(b, a + 1):
            summa += i
    print('The sum of the numbers:', summa)


summ(6, 2)