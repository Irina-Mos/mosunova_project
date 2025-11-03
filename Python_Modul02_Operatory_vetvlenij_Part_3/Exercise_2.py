x = int(input('Enter a six-digit integer: '))
if x // 100000 != 0 and x // 100000 < 10:
    units = x % 10
    tens = x % 100 // 10
    hundreds = x % 1000 // 100
    thousands = x % 10000 // 1000
    tens_of_thousands = x % 100000 // 10000
    hundreds_of_thousands = x // 100000
    y = hundreds_of_thousands + tens_of_thousands * 10 + thousands * 1000 + hundreds * 100 + tens * 10000 + units * 100000
    print(y)
else:
    print('Invalid input')