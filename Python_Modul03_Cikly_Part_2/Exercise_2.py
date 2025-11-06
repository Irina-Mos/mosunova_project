x = int(input('Enter natural number: '))
if x > 0:
    total = 1
    for i in range(1, x + 1):
        total *= i
    print('Factorial =', total)
else:
    print('Invalid input')