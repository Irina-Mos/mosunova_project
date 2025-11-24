import random
num_of_num = random.randint(1, 10)
num_list = []
sum_neg = 0
sum_even = 0
sum_odd = 0
tot_ind_mult_3 = 1
pos_list = []
sum_pos = 0
for i in range(0, num_of_num):
    num = random.randint(-10, 10)
    num_list.append(num)
    if num < 0:
        sum_neg += num
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
    if i % 3 == 0 and i != 0:
        tot_ind_mult_3 *=num
    if num > 0:
        pos_list.append(i)
print(num_list)
# №1
print('The sum of negative numbers:', sum_neg)
# №2
print('The sum of even numbers:', sum_even)
# №3
print('The sum of odd numbers:', sum_odd)
# №4
if tot_ind_mult_3 == 1:
    print('Product of elements with indices multiple of 3: 0')
else:
    print('Product of elements with indices multiple of 3:', tot_ind_mult_3)
# №5
max_el = max(num_list)
min_el = min(num_list)
print('The product of the elements between the min and the max element:', max_el * min_el)
# №6
if len(pos_list) == 0:
    print('The sum of the elements between the first and last positive elements: 0')
else:
    for i in range(pos_list[0] + 1, pos_list[-1]):
        sum_pos += num_list[i]
    print('The sum of the elements between the first and last positive elements:',sum_pos)
