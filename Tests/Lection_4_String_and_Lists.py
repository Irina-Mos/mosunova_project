#String
string = "Hello World!"
print(string)
# ID строки
print(id(string))
# Раскодировка строки
# encode_string = string.encode('utr-16')
# print(encode_string)

#Сложение строк
string_1 = "Hello"
string_2 = 'World'
print(string_1 + " ", string_2)
# Умножение на число
print(string_1 * 5)
# Индекс
print(string[-1])
print(string[0])
# Длина строки
l = len(string)
print(l)
# Проверка всех элементов строки
# for i in range(0, len(string) + 1):
#     if string[i] == 'o':
#         print('Мы нашли "о"')

# Методы изменения регистра строк
#Переводит первый символ в верхний регистр
print(string.capitalize())
#Переводит все символы в нижний регистр
print(string.lower())
#Переводит все символы в верхний регистр
print(string.upper())
#Переводит первый символы каждого слова на верхний регистр
print(string.title())
#Меняет регистр на противоположный
print(string.swapcase())

# Методы проверки строк
# Проверяет, состоит ли строка только из цифр и букв
print(string.isalnum())
# Проверяет, состоит ли строка только из букв
print(string.isalpha())
# Проверяет, состоит ли строка только из цифр
print(string.isdigit())
# Проверяет, все ли буквы в нижнем регистре
print(string.islower())
# Проверяет, все ли буквы в верхнем регистре
print(string.isupper())
# Проверяет, является ли строка пробелом
print(string.isspace())
# Проверяет, первая буква каждого слова в верхнем регистре
print(string.istitle())
