# # Изменяемые и неизменяемые типы данных
# # Неизменяемые типы данных
# var_str = 'Hello'
# var_int = 10
# var_tuple = (1, 2, 3)
# # Изменяемый тип данных
# var_list = [1, 2, 3]
# val_dict = {'key': 'value'}
# print(id(var_int))
# var_list.append(4)
# print(id(var_list))
# # Перезапись данных
# counter = 0
# for i in range(1, 10):
#     counter += 1
#     print(id(counter))
# # Тройные ковычки
# a = """
# print "Hello"
# """
# print(a)
# # Срезы или слайсы строк. string[start:stop:step]
# var_str = 'Hello World'
# # С первого по четвертый
# print(var_str[:4])
# # С четвертого символа по последний
# print(var_str[3:])
# # С третьего символа по предпоследний
# print(var_str[2:-1])
# # Инвертировать строку (вывести наоборот
# print(var_str[::-1])
# # Пример: выйдет 3, 5, 7; 9,7,5; в обратном порядке
# var_int = '1234567890'
# print(var_int[2:8:2])
# print(var_int[8:2:-2])
# print(var_int[::-1])
# #Проверка вхождения строки в другую строку
# print("World" in var_str)
# # Сложение и умножение строк
# s = "AB"
# s = s * 2 + "CD"
# print(s)
# # Определить тип данных
# age = input()
# print(type(age))
# # Является ли слово палиандромом
# text = input()
# text = text.lower()
# if text == text[::-1]:
#     print('Это палиандром')
# else:
#     print('Это не палиандром')
# # Запрос имени пользователя и вывод его в рамочке из *
# name = input('Enter your name: ')
# stars = '*' * len(name) + 4 * '*'
# print(stars)
# print('* ' + name + ' *')
# print(stars)
# # Списки
# # Ввод вручную
# val_list = [1, 'int', 3.0, True, [1, 2]]
# a = "Hello World"
# # Преобразовать строку в лист и обратно, но в виде списка
# a_list = list(a)
# print(a_list)
# a_str = str(a_list)
# print(a_str)
# # Список из чисел от 1 до 9
# a_list = list(range(1, 10))
# print(a_list)
# # Пустой список
# b = list()
# b = []
# #Изменение объектов
# fruits = ['яблоко', 'апельсин', 'банана', 'ананасик']
# fruits[2] = 'банан'
# print(fruits)
# # Добавление в список в конце
# fruits.append('помидор')
# print(fruits)
# #Добавление в список в указанное место
# fruits.insert(0, 'лимон')
# print(fruits)
# # Добавление одного списка или строки в другой
# a = ['a', 'b']
# b = 'Hello'
# fruits.extend(a)
# fruits.extend(b)
# print(fruits)
# # Сложение и умножение
# fr = fruits + a
# print(fruits * 2)
# # Удаление объектов
# fruits.remove('яблоко')
# fruits.pop(0)
# print(fruits)
# #Проверка вхождения в список
# if 'яблоко' in fruits:
#     print('яблоко это фрукт')
# # Матрица
# matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# matrix.append([1, 2, 3])
# print(matrix)
# Задание: создать список из чисел: добавить число в конце, в начале. Удалить первое число, удалить последнее число, проверить вхождение чила в список
numbers = [3, 5, 7, 3, 4, 6, 1, 9]
print(numbers)
numbers.append(10)
print(numbers)
numbers.insert(0, 1)
print(numbers)
numbers.pop(0)
print(numbers)
numbers.pop()
print(numbers)
if 5 in numbers:
    print('В списке есть 5')
else:
    print('В списке нет 5')