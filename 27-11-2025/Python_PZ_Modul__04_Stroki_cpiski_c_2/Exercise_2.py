import random
def operations(num_of_num):
    # num_of_num = random.randint(1, 10)
    num_list = []
    count_neg = 0
    count_pos = 0
    count_zero = 0
    for i in range(0, num_of_num):
        num = random.randint(-10, 10)
        num_list.append(num)
        if num < 0:
            count_neg += 1
        elif num > 0:
            count_pos += 1
        elif num == 0:
            count_zero += 1
    print('List:', num_list)
    max_el = max(num_list)

    print('Maximum list item:', max_el)
    min_el = min(num_list)
    print('Minimum list item:', min_el)

    print('The number of positive numbers:', count_pos)
    print('The number of negative numbers:', count_neg)
    print('The number of zeros:', count_zero)


operations(random.randint(1, 10))