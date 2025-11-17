val = input('Enter the string : ')
counter_alpha = 0
counter_digit = 0
for i in range(0, len(val)):
    n = val[i]
    if n.isalpha():
        counter_alpha += 1
    if n.isdigit():
        counter_digit += 1
print('There are', counter_alpha, 'letters in the string.')
print('There are', counter_digit, 'digits in the string.')
