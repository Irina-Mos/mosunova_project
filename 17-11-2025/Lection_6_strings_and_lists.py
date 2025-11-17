# Строки и списки
str = 'text123/'
list = ['text', str, 123]
print(id(list))
print(list)
list[2] = 5678
print(list)
print(id(list))
print(list[::-1])
# Копия списка
list2 = list[:]
print(list2)
list2[0] = 'new text in list2'
print(list)
print(list2)
# Операции над списками
# Объединение (сложение) и умножнение
list3 = list + list2
print(list3 * 3)
#Вхождение в список
print('text' in list3)
#Вложенные списки
included_lists = [[1, 2, 3, 4], ['text1','text2']]
print(included_lists[0][1])
# Перебор элементов
for obj in included_lists:
    for subject in obj:
        print(subject)
# Методы списков
# Добавление в конец списка элемента
my_list = []
my_list.append('text1')
print(my_list)
# Добавление иттерируемых объектов (ряд элемементов)
my_list.extend(['string', 1, 2, 3])
print(my_list)
#Добавление объекта по индексу
my_list.insert(0, 'text2')
print(my_list)
#Удаление объекта по значению объета
my_list.remove(1)
print(my_list)
# Удаление объекта по индексу
my_list.pop(0)
print(my_list)
# Очистка списка
my_list.clear()
print(my_list)
# Подсчет вхождения элементов в список
val = my_list.count(1)
# Сортировка списка (true - по возрастанию, false - убыванию)
my_list.sort(reverse=True)
print(my_list)
# Перевернуть список
my_list.reverse()
# Перебор списка с помощью while
counter = 0
while counter < len (my_list):
    val = my_list[counter]
    if val == 4:
        print('We find 4')
        break
    counter += 1
