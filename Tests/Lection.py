# IF-ELSE
# var = 7
# my_bool = var > 8
# print(my_bool)
# if my_bool == False:
#     print('Hello')
# else:
#     print('Bye')

# AND
# x = 5
# if x > 0 and x < 10:
#     print('0 < x < 10')

# OR
# x = 15
# if x < 0 or x > 10:
#     print('x < 0 or x > 10')

# NOT
# day = 'Monday'
# prazdnik = True
# if day == 'Monday' and prazdnik:
#     print('Сегодня отдыхаем!')
# else:
#     print('Сегодня работаем.')

# IFELSE
# x = 0
# if x % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')

# ELIF
# age = int(input('Возраст: '))
# if age < 7:
#     print('Вы школьник')
# elif age < 15:
#     print('Вы все еще школьник')
# elif age <= 18:
#     print('Вы почти не школьник')
# elif age < 25:
#     print('Пора работать')
# else:
#     print('Вы пенсионер')

# Вложенные циклы
is_raining = True
temp = -1
if is_raining:
    if temp < 0:
        print('Идет снег')
    else:
        print('Идет дождь')
else:
    if temp > 0:
        print('Осадков нет, но тепло')
    else:
    print('Осадков нет, но холодно')