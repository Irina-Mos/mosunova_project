# Регулярные выражения
# \d+
# \d*
import re

# text = 'I live in 2025'
# pattern = re.compile(r"\d+")
# #
# val = re.search(pattern, text)
# #
# re.match(pattern, text)
# #
# re.findall(pattern, text)
# #
# re.fullmatch(pattern, text)
# #
# re.finditer(pattern, text)
# #
# re.split(pattern, text, maxsplit=1)
# #
# re.sub(pattern, repl="text", string=text, count=1)

#Задание №1
text_1 = "+79082733977"
text_2 = "89082733977"
pattern = re.compile(r"(\+7|8)\d{10}")
val = re.search(pattern, text_2)
print(val.group(), val.start(), val.end())
# Задание 2. Достать из текста слово полученное от пользователя
text = input('Enter the text: ')
word_str = input('Enter the words separated by commas: ')
word_list = word_str.split(',')
print(word_list)
itog = []
for word in word_list:
    pattern = re.compile(rf"\b{word}\b")
    val = re.findall(pattern, text)
    itog += val
print(itog)
# Задание 3. Соответствует ли строка формату даты ДД.ММ.ГГГГ
# ДД - от 1 до 31, ММ от 1 до 12, ГГГГ любые цифры
# Задание 4. Убрать все пробелы из строки