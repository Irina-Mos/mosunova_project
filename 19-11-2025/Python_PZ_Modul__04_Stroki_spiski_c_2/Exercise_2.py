num_str = input('Enter the integers separated by commas: ')
num_search = input('Enter an integer to search in the list: ')
num_list = num_str.split(',')
print(num_list)
counter = 0
for i in range(0, len(num_list)):
    if num_search == num_list[i]:
        counter += 1
print('Number', num_search, 'occurs', counter, 'times')
