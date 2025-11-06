x = int(input('Enter the first boundary of the range: '))
y = int(input('Enter the second boundary of the range: '))
num = int(input('Enter a number in this range: '))
if x < y:
    while num < x or num > y:
        num = int(input('Enter a number in this range: '))
    for i in range(x, y + 1):
        if i == num:
            print('!', i, '!', end=' ')
        else:
            print(i, end=' ')
elif x == y:
    while num != x:
        num = int(input('Enter a number in this range: '))
    print('!', x, '!')
else:
    while num > x or num < y:
        num = int(input('Enter a number in this range: '))
    for i in range(y, x + 1):
        if i == num:
            print('!', i, '!', end=' ')
        else:
            print(i, end=' ')