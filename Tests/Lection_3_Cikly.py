# bool(0)
# bool("")
# bool(None)
# bool([])
# bool({})
# bool(())

#Цикл while
#№1 Вывести фразу определенное количество раз
# counter = 5
# while counter != 0:
#     print('Hello')
#     counter -= 1

#№2 Вывести числа от 1 до заданного числа
# x = int(input('Enter natural number: '))
# counter = 1
# if x > 0:
#     while counter != x + 1:
#         print(counter)
#         counter += 1
# else:
#     print('Invalid input')

#№3 Вывести сумму чисел от 1 до заданного числа
# x = int(input('Enter natural number: '))
# counter = 1
# summa = 0
# if x > 0:
#     while counter != x + 1:
#         summa += counter
#         counter += 1
#     print('Sum =', summa)
# else:
#     print('Invalid input')

# #Цикл for
#№1 Выводит числа от 0 до 10
# for i in range(11):
#     print(i)
#
#№2 Выводит числа от 1 до 9
# for i in range(1, 10):
#     print(i)
#
#№3 Выводит все объекты из списка
# for i in [1, 2, 3, 4, 'num', 'more']:
#     print(i)
#Вывод чисел от 0 до 10 с помощью while
# i = 0
# while i < 11:
#     print(i)
#     i += 1

#Range
# for i in range(1, 100, 2):
#     print(i)

#Со строками
# val = "Python"
# for i in val:
#     print(i)
#
# val = "Python"
# val_2 = ''
# for i in val:
#     val_2 += i + "*"
# print(val_2)

#Остановка цикла break
# var = 'Hello, its a break'
# for i in [1, 2, 3, 52, 2, 3]:
#     print(i)
#     if i == 52:
#         break
# print(var)
# №4 Вывести числа от 1 до заданного числа
# x = int(input('Enter natural number: '))
# if x > 0:
#     for i in range(1, x + 1):
#         print(i)
# else:
#     print('Invalid input')
#Оператор continue
# for i in range(1, 101):
#     if i % 2 == 0:
#         continue
#     print(i)

numbers = [1, 3, 5, 8, 7, 9, 10]
for num in numbers:
    print(num)
    if num == 7:
        print('Ура, мы нашли число 7')
        break
else:
    print('К сожалению, числа 7 там нет')
