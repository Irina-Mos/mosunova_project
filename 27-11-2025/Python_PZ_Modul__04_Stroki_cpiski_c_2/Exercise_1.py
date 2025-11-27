# expression = input('Enter the arithmetic expression: ')
def operations(expression):
    num_1 = ''
    operation = ''
    num_2 = ''
    i = 0
    counter = 0
    while expression[i] != '+' and expression[i] != '-' and expression[i] != '*' and expression[i] != '/':
        num_1 += expression[i]
        i += 1
        counter += 1
    # print(num_1)
    for i in range(0, len(expression)):
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*' or expression[i] == '/':
            operation += expression[i]
    # print(operation)
    for i in range(counter + 1, len(expression)):
        num_2 += expression[i]
    # print(num_2)
    if operation == '+':
        print('The sum of the numbers:', int(num_1) + int(num_2))
    elif operation == '-':
        print('The difference of numbers:', int(num_1) - int(num_2))
    elif operation == '*':
        print('The product of numbers:', int(num_1) * int(num_2))
    elif operation == '/':
        print('The quotient of a numbers:', int(num_1) / int(num_2))


operations('23+12')
operations('23-12')
operations('40*4')
operations('40/4')