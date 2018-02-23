# ЗАДАЧИ НА ДЕКОРАТОРЫ


# 1. Написать декоратор, отменяющий выполнение любой декорированной функций и пишет в консоль: ИМЯ_ФУНКЦИИ is canceled!
from collections import Counter
from time import time


def my_decorator(func):
    def inner(*args):
        print(func.__name__, 'is canceled!')

    return inner


@my_decorator
def print_your_name(name: str) -> None:
    print('Your name is', name)


print_your_name('Arthur')


# 2. Реализовать декоратор, который измеряет скорость выполнения функций.
def time_measure(func):
    def inner(*args, **kwargs):
        a = time()
        func()
        print(func.__name__, 'was performed in {} seconds.'.format(time() - a))
    return inner


@time_measure
def some_func():
    for i in range(0, 10000000):
        a = i + i / 2


some_func()
# 3. Реализовать декоратор, который будет считать, сколько раз выполнялась функция
def count_run_func(func):
    c = Counter()
    def inner(*args, **kwargs):
        func(*args)
        name = func.__name__
        c[name] += 1
        print('Function {} was run {} times!'.format(name, c[name]))

    return inner


@count_run_func
def first_func(a, b):
    return a + b


@count_run_func
def second_func(a, b):
    return a - b


first_func(3, 5)
second_func(4, 6)
first_func(2, 98)
first_func(3, 223)
second_func(-12, 23)

# 4. Реализовать декоторатор, который будет логгировать процесс выполнения функции: создан декоратор, начато выполнение функции, закончено выполнение функции
def logging(func):
    def inner(*args, **kwargs):
        print('Decorator created!', 'Start to run function...', sep='\n')
        func(*args)
        print('Function execution is completed!')

    return inner


@logging
def sum_three_numbers(a, b, c):
    print(a + b + c)


sum_three_numbers(50, 23, 77)
# 5. Реализовать декоратор, который будет перехватывать все исключения в функции. Если они случились, нужно просто писать в консоль сообщение об ошибке
def handle_exceptions(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as err:
            print('{} was thrown!'.format(err.__repr__()))
    return inner


@handle_exceptions
def multiply_three_numbers(a, b, c):
    raise ValueError

multiply_three_numbers(2, 2, 2)
