num_str = input('Enter the integers separated by commas: ')
num_list = num_str.split(',')
counter = 0
summa = 0
for i in range(0, len(num_list)):
    summa += int(num_list[i])
    counter += 1
print('The sum of the numbers:', summa)
print('The arithmetic mean of numbers: ', summa/counter)