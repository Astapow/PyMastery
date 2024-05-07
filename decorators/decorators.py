def decorator(func):
    def wrapper(*args, **kwargs):
        print("i'm here ")
        params = [item ** 3 if isinstance(item, int) else item.lower() for item in args]
        print(params)  # ["hello", "world"]
        return func(*params, **kwargs)

    return wrapper


@decorator
def sey_hello(param1, param2):
    print(f"Hello World!\n1: {param1}\n2: {param2}")


@decorator
def main():
    pass


# sey_hello("Hello", "World")
# print(sey_hello)
# print(main)


import functools


def decorator2(func):
    @functools.wraps(func)
    def wrapper2(*args, **kwargs):
        print("i'm here")
        params = [item ** 2 if isinstance(item, int) else item.capitalize() for item in args]
        return func(*params, **kwargs)

    return wrapper2


@decorator2
def sey_hello2(param1: str, param2: int):
    print(f"Hello World!\n1: {param1}\n2: {param2}")


# print(sey_hello2)


def stop_words(words: list):  # ["hello", "world", "black", "red"]
    def decorator_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # def some_function(param1, param2, param3):

            refactory_list = []
            for arg in args:
                if arg in words:
                    print(f"{arg} is in {words}")
                    arg = "stop"

                elif arg not in words:
                    print(f"{arg} is not in {words} good job")

                refactory_list.append(arg)

            return func(*refactory_list, **kwargs)

        return wrapper

    return decorator_func


@stop_words(["hello", "world", "black", "red"])
def some_function(param1, param2, param3):
    return f"{param1} + {param2} + {param3}"


# print(some_function("hello", "world", 2))


# print(some_function)

# ################ @staticmethod @classmethod

class MyClass:
    def instancemethod(self):
        return 'instance method called', self

    @staticmethod
    def sey_hello(name, age):
        return f'static method called: {name} with age {age}'

    @classmethod
    def class_method(cls):
        return 'class method called', cls


class A(MyClass):
    @classmethod
    def class_method(cls):
        return 'class method @@@@@@@', cls


# obj = MyClass()
# # print(obj.instancemethod())
# # print(obj.sey_hello("Ivan", 21))
# print(MyClass.class_method())
# print(A.class_method())


# ################

# ################ @property
class MyClass2:
    age = 21

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def some_method(self):
        return "@@@@"


second = MyClass2("John", "Doe")
print(second.full_name)
print(second.age)
second.age = 19
print(second.age)
# print(second.some_method())
# second.full_name = "Ivan Ivanov"
"""
Практика:

1. Напишите декоратор который логирует результат выполнения функции в файл.
2. Напишите декоратор который измеряет время выполнения программы.
3. Напишите декоратор который возвращяет хешированое значение функции.
4. Создайте декоратор для обработки исключений, возникающих внутри функции, и вывода информации об ошибке.
5. Напишите декоратор, который будет проверять типы аргументов, переданных в функцию.

6. Создайте декоратор @check_input_types, который принимает аргументы - типы ожидаемых входных данных для функции.
    Декоратор должен проверять переданные в функцию аргументы на соответствие указанным типам.
     
7. Напишите декоратор @repeat_execution, который принимает параметр times - количество раз,
 которое функция должна быть выполнена. Если параметр не указан, функция должна выполняться бесконечно.
 
8. Напишите класс TypeDecorators, и методы у него.
methods:

to_int

to_str

to_bool

to_float

@TypeDecorators.to_int
def do_nothing(string: str):

    return string

 

@TypeDecorators.to_bool
def do_something(string: str):

    return string
"""
