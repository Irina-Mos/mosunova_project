x = int(input('Enter the first boundary of the range: '))
y = int(input('Enter the second boundary of the range: '))
counter = 0
counter_5 = 0
if x < y:
    print('1. All numbers in the range:', end=' ')
    for i in range(x, y + 1):
        print(i, end=' ')
    print('\n2. All numbers in the range are in descending order:', end=' ')
    for i in range(y, x - 1, -1):
        print(i, end=' ')
    print('\n3. Numbers multiples of 7:', end=' ')
    for i in range(x, y + 1):
        if i % 7 == 0:
            print(i, end=' ')
            counter += 1
    if counter == 0:
        print('There are no numbers in the range that are multiples of 7.', end=' ')
    print('\n4. The number of numbers that are multiples of 5:', end=' ')
    for i in range(x, y + 1):
        if i % 5 == 0:
            counter_5 += 1
    print(counter_5, end=' ')
elif x == y:
    print('1. All numbers in the range:', x,end=' ')
    print('\n2. All numbers in the range are in descending order:', x, end=' ')
    print('\n3. Numbers multiples of 7:', end=' ')
    if x % 7 == 0:
        print(x, end=' ')
        counter += 1
    if counter == 0:
        print('There are no numbers in the range that are multiples of 7.', end=' ')
    print('\n4. The number of numbers that are multiples of 5:', end=' ')
    if x % 5 == 0:
        counter_5 += 1
    print(counter_5, end=' ')
else:
    print('1. All numbers in the range:', end=' ')
    for i in range(y, x + 1):
        print(i, end=' ')
    print('\n2. All numbers in the range are in descending order:', end=' ')
    for i in range(x, y - 1, -1):
        print(i, end=' ')
    print('\n3. Numbers multiples of 7:', end=' ')
    for i in range(y, x + 1):
        if i % 7 == 0:
            print(i, end=' ')
            counter += 1
    if counter == 0:
        print('There are no numbers in the range that are multiples of 7.', end=' ')
    print('\n4. The number of numbers that are multiples of 5:', end=' ')
    for i in range(y, x + 1):
        if i % 5 == 0:
            counter_5 += 1
    print(counter_5, end=' ')