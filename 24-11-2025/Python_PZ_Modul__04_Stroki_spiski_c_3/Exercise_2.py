import random
num_of_num = random.randint(1, 10)
num_list = []
neg_list = []
pos_list = []
even_list = []
odd_list = []
for i in range(0, num_of_num):
    num = random.randint(-10, 10)
    num_list.append(num)
    if num < 0:
        neg_list.append(num)
    elif num > 0:
        pos_list.append(num)
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print('List:', num_list)
print('Even numbers:', even_list)
print('Odd numbers:', odd_list)
print('Positive numbers:', pos_list)
print('Negative numbers:', neg_list)