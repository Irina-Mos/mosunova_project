x = int(input('Enter natural number: '))
if x > 0:
    for i in range(1, 11):
        print(x, '*', i, '=', x * i)
        i += 1
else:
    print('Invalid input')