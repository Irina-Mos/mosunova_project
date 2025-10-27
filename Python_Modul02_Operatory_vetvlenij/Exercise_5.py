# Задание №5
x = int(input('Enter number 1: '))
y = int(input('Enter number 2: '))
arithmetic_op = input('Enter arithmetic operation: Sum(+), Difference(-), Arithmetic mean or Product of number(*).\n')
if arithmetic_op == 'Sum' or arithmetic_op == '+':
    print('Sum:', x + y)
elif arithmetic_op == 'Difference' or arithmetic_op == '-':
    print('Difference:', x - y)
elif arithmetic_op == 'Arithmetic mean':
    print('Arithmetic mean:', (x + y) / 2)
elif arithmetic_op == 'Product of number' or arithmetic_op == '*':
    print('Product of number:', x * y)
else:
    print('Entered incorrectly.')