x = int(input('Enter the first boundary of the range: '))
y = int(input('Enter the second boundary of the range: '))
counter = 0
counter_5 = 0
if x < y:
    for i in range(x, y + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizz Buzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
elif x == y:
    if x % 3 == 0 and x % 5 == 0:
        print('Fizz Buzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
else:
    for i in range(y, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizz Buzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)