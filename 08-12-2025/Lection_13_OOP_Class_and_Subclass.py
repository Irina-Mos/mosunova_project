# Процедурное программирование
# stack_list = []
#
# def push(val):
#     stack_list.append(val)
#
# def pop():
#     val = stack_list[-1]
#     stack_list.pop()
#     return val
#
# push(3)
# push(5)
# push(10)
# # print(stack_list)
# # print(pop())
# # print(stack_list)
# # ООП
# #
# # class SimpleClass:
# #     pass
# #
# #
# # my_first_object = SimpleClass()
# # print(my_first_object)
#
# class Stack:
#     counter = 0
#     def __init__(self):
#         Stack.counter += 1
#         self.first = 1
#         self.__stack_list = []
#         self.__stack_list_2 = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         self.__stack_list.pop()
#         return val
#
#     def set_second(self):
#         self.second = 2
#
#
# stack_obj = Stack()
# stack_obj.set_second()
# print(stack_obj.__dict__)
#
# stack_obj_2 = Stack()
# # stack_obj_2.set_second()
# print(stack_obj_2.__dict__)
#
# print(getattr(stack_obj, "first"))
# # stack_obj._Stack__stack_list_2.append(100)
# # stack_obj.stack_list.append(100)
# # stack_obj.push(3)
# # stack_obj.push(156)
# # stack_obj.push(734)
# # stack_obj_2.push(100)
# #
# # print(stack_obj.pop())
# # print(stack_obj_2.pop())
# # print(stack_obj.__dict__)
# # print(stack_obj_2)
#
# print("Counter =", Stack.counter)
#
# # Наследование классов
# class SuperClass:
#     pass
#
# class Subclass(SuperClass):
#     pass

# Пример: животные

class Animal:
    def __init__(self):
        self.can_breath = True
        self.average_age = 20
        self.animal_sound = "..."

    def get_animal_info(self):
        print(f"Base info: все животные дышат: {self.can_breath}, их средний возраст равен: {self.average_age}.")

class Mammals(Animal):
    def __init__(self, eyes_count):
        super().__init__()
        self.feet_count = 4
        self.eyes_count = eyes_count



class Cats(Mammals):
    def __init__(self, eyes_count, name):
        super().__init__(eyes_count=eyes_count)
        self.name = name
        self.animal_sound = "meow"

    # def get_cat_info(self):
    #     print(f"Коты имеют {self.feet_count} ног, издают звук: {self.animal_sound}, имеют количество глаз равное: {self.eyes_count}. "
    #           f"В среднем живут {self.average_age} лет")

    def get_cat_info(self):
        self.get_animal_info()
        print(f"Кошку зовут: {self.name}, она имеет {self.eyes_count} глаз, у нее {self.feet_count} ног.")


cats = Cats(eyes_count=1, name="Masha")
cats.get_cat_info()

cats = Cats(eyes_count=2, name="Barsik")
cats.get_cat_info()
# mammals = Mammals()
# print(mammals.__dict__)