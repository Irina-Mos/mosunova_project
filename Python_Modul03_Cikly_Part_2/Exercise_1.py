x = int(input('Enter number 1: '))
y = int(input('Enter number 2: '))
if x < y:
    summa = 0
    counter = 0
    for i in range(x, y + 1):
        summa += i
        counter += 1
elif x == y:
    summa = x
    counter = 1
else:
    summa = 0
    counter = 0
    for i in range(y, x + 1):
        summa += i
        counter += 1
print('Sum =', summa)
print('Arithmetic mean =', summa / counter)
