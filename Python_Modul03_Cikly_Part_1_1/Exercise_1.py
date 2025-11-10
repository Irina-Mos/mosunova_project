x = int(input('Enter the first boundary of the range: '))
y = int(input('Enter the second boundary of the range: '))
counter = 0
if x < y:
    for i in range(x, y + 1):
        if i % 7 == 0:
            print(i)
            counter += 1
elif x == y:
    if x % 7 == 0:
        print(x)
        counter += 1
else:
    for i in range(y, x + 1):
        if i % 7 == 0:
            print(i)
            counter += 1
if counter == 0:
    print('There are no numbers in the range that are multiples of 7.')