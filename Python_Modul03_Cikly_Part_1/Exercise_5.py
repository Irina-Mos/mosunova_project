x = int(input('Enter number 1: '))
y = int(input('Enter number 2: '))
if x < y:
    for i in range(x, y + 1):
        if i % 2 != 0:
            print(i)
elif x == y:
    if x % 2 != 0:
        print(x)
else:
    for i in range(y, x + 1):
        if i % 2 != 0:
            print(i)