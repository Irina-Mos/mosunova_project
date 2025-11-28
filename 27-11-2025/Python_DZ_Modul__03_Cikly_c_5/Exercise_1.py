# x = int(input('Enter the side of the square: '))
import math
# Рис. А
def square_a(x):
    counter_j = 0
    counter_n = x
    for i in range(0, x):
        for n in range(counter_n, x):
            print(' ', end=' ')
        counter_n -= 1
        for j in range(counter_j, x):
            print('*', end=' ')
        print('\n', end='')
        counter_j += 1

print("Рисунок 1.а")
square_a(5)

# Рис. Б
def square_b(x):
    counter = x
    for i in range(0, x):
        for j in range(x, counter - 1, -1):
            print('*', end=' ')
        print('\n', end='')
        counter -= 1

print("Рисунок 1.б")
square_b(5)

# Рис. В
def square_v(x):
    counter_j = x
    counter_n = 0
    for i in range(0, math.ceil(x / 2)):
        for n in range(0, counter_n):
            print(' ', end=' ')
        counter_n += 1
        for j in range(0, counter_j):
            print('*', end=' ')
        print('\n', end='')
        counter_j -= 2
    for i in range(math.ceil(x / 2), x):
        print('\n', end=' ')

print("Рисунок 1.в")
square_v(5)

# Рис. Г
def square_g(x):
    if x % 2 == 0:
        counter_j = 2
        counter_n = math.floor(x / 2) - 1
    else:
        counter_j = 1
        counter_n = math.floor(x / 2)
    for i in range(0, math.floor(x / 2)):
        print('\n', end='')
    for i in range(math.floor(x / 2), x):
        for n in range(0, counter_n):
            print(' ', end=' ')
        counter_n -= 1
        for j in range(0, counter_j):
            print('*', end=' ')
        print('\n', end='')
        counter_j += 2

print("Рисунок 1.г")
square_g(6)

# Рис. Д
def square_d(x):
    counter_j = x
    counter_n = 0
    for i in range(0, math.floor(x / 2)):
        for n in range(0, counter_n):
            print(' ', end=' ')
        counter_n += 1
        for j in range(0, counter_j):
            print('*', end=' ')
        print('\n', end='')
        counter_j -= 2

    if x % 2 == 0:
        counter_j = 2
        counter_n = math.floor(x / 2) - 1
    else:
        counter_j = 1
        counter_n = math.floor(x / 2)
    for i in range(math.floor(x / 2), x):
        for n in range(0, counter_n):
            print(' ', end=' ')
        counter_n -= 1
        for j in range(0, counter_j):
            print('*', end=' ')
        print('\n', end='')
        counter_j += 2

print("Рисунок 1.д")
square_d(7)

# Рис. Е
def square_e(x):
    counter_j = 1
    counter_n = x - 2
    for i in range(0, math.floor(x / 2)):
        for j in range(0, counter_j):
            print('*', end=' ')
        for n in range(0, counter_n):
            print(' ', end=' ')
        counter_n -= 2
        for j in range(0, counter_j):
            print('*', end=' ')
        counter_j += 1
        print('\n', end='')

    if x % 2 == 0:
        counter_n += 2
        counter_j -= 1
        for i in range(math.floor(x / 2), x):
            for j in range(0, counter_j):
                print('*', end=' ')
            for n in range(0, counter_n):
                print(' ', end=' ')
            counter_n += 2
            for j in range(0, counter_j):
                print('*', end=' ')
            counter_j -= 1
            print('\n', end='')
    else:
        counter_n += 2
        counter_j -= 1
        print('* ' * x)
        for i in range(math.floor(x / 2) + 1, x):
            for j in range(0, counter_j):
                print('*', end=' ')
            for n in range(0, counter_n):
                print(' ', end=' ')
            counter_n += 2
            for j in range(0, counter_j):
                print('*', end=' ')
            counter_j -= 1
            print('\n', end='')

print("Рисунок 2.е")
square_e(11)

# Рис. Ж
def square_zh(x):
    counter_j = 1
    counter_n = x
    for i in range(0, math.floor(x / 2)):
        for j in range(0, counter_j):
            print('*', end=' ')
        counter_j += 1
        for n in range(0, counter_n - 1):
            print(' ', end=' ')
        counter_n -= 1
        print('\n', end='')
    if x % 2 == 0:
        counter_j -= 1
    for i in range(math.floor(x / 2), x):
        for j in range(0, counter_j):
            print('*', end=' ')
        counter_j -= 1
        for n in range(0, counter_n):
            print(' ', end=' ')
        counter_n += 1
        print('\n', end='')

print("Рисунок 2.ж")
square_zh(16)

# Рис. З
def square_z(x):
    counter_j = 1
    counter_n = x - 1
    for i in range(0, math.floor(x / 2)):
        for n in range(0, counter_n):
            print(' ', end=' ')
        counter_n -= 1
        for j in range(0, counter_j):
            print('*', end=' ')
        counter_j += 1
        print('\n', end='')
    if x % 2 == 0:
        counter_n += 1
        counter_j -= 1
    for i in range(math.floor(x / 2), x):
        for n in range(0, counter_n):
            print(' ', end=' ')
        counter_n += 1
        for j in range(0, counter_j):
            print('*', end=' ')
        counter_j -= 1
        print('\n', end='')

print("Рисунок 2.з")
square_z(7)

# Рис. И
def square_i(x):
    counter = 0
    for i in range(0, x):
        for j in range(counter, x):
            print('*', end=' ')
        print('\n', end='')
        counter += 1

print("Рисунок 2.и")
square_i(5)

# Рис. К
def square_k(x):
    counter_j = 1
    counter_n = x - 1
    for i in range(0, x):
        for n in range(0, counter_n):
            print(' ', end=' ')
        counter_n -= 1
        for j in range(0, counter_j):
            print('*', end=' ')
        print('\n', end='')
        counter_j += 1

print("Рисунок 2.к")
square_k(5)