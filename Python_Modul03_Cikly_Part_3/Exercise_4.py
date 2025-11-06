import random
from datetime import datetime
num = random.randint(1, 500)
counter = 0
x = int(input('Guess the number: '))
now_1 = datetime.now().time
while x != num:
    if x < num:
        print()
    elif x > num:
        print()
    elif x == 0:
        break
    else:
        x = int(input('Guess the number: '))
    num = x
    counter += 1
now_2 = datetime.now().time
time = now_2 - now_1
print(counter, time)
