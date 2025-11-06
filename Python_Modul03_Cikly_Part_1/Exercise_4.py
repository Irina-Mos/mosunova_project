x = int(input('Enter number 1: '))
y = int(input('Enter number 2: '))
if x < y:
    for i in range(y, x - 1, -1):
        print(i)
elif x == y:
    print(x)
else:
    for i in range(x, y - 1, -1):
        print(i)