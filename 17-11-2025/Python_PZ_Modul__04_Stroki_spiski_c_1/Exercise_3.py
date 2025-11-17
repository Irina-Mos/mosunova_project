val = input('Enter the string : ')
symb = input('Enter the symbol: ')
counter = 0
for i in range(0, len(val)):
    if symb == val[i]:
        counter += 1
print('There are', counter, 'symbols in the string.')