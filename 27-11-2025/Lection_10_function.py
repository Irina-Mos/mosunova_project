# Функции с параметрами
def some_function(number_1, number_2):
    a = number_1 + number_2
    print(a)

some_function(number_1=10, number_2=30)
# Функция с параметрами по умолчанию
def greetings(name, age = 20):
    print(f'Hello, {name}')
    print(age)
greetings('John')
#Return - завершает функцию и возвращает определнное значение
def some_function(number_1, number_2):
    a = number_1 + number_2
    if a > 100:
        return a
    else:
        return False

val = some_function(number_1=100, number_2=30)
print(val)
# Привер: вывести квадрат числа
def square(number):
    a = number * number
    return a

sqr_num = square(20)
print(sqr_num)
# Глобальная переменная
global_value = 0

def some_function(number_1, number_2):
    a = number_1 + number_2


val = some_function(number_1=100, number_2=30)
print(val)