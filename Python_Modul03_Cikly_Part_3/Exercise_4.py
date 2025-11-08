import random
from datetime import datetime
num = random.randint(1, 500)
print(num)
counter = 1
now_1 = datetime.now()
x = int(input('Guess the number: '))
if x != num and x != 0:
    while x != num and x != 0:
        if x < num:
            print('The number is less than the desired one')
            x = int(input('Guess the number: '))
        elif x > num:
            print('The number is more than the desired one')
            x = int(input('Guess the number: '))
        counter += 1
elif x == num:
    print('You guessed the number')
elif x == 0:
    print('You have completed the game.\nThe hidden number:', num)
    counter = 0
if x != 0 and counter > 1:
    print('You guessed the number')
elif x == 0 and counter > 1:
    print('You have completed the game.\nThe hidden number:', num)
    counter -= 1
now_2 = datetime.now()
time = now_2 - now_1
print('Number of attempts:',counter)
print('Time spent:', time)
