# Написать генератор, который бы каждый раз возвращал новое случайное число
import random
from collections import Iterable

import sys


def gen1():
    while True:
        yield random.randint(-sys.maxsize, sys.maxsize)

x_random = gen1()
print(next(x_random))
print(next(x_random))


# Написать генератор, который бы работал как range()
def custom_range(a, b, c = 1):
    while a < b:
        yield a
        a += c


x_range = custom_range(0, 10, 2)
print(next(x_range))
print(next(x_range))
print(next(x_range))


# Написать генератор, который бы работал как map()
def custom_map(func, some_iter):
    for i in some_iter:
        yield func(i)


def work(value):
    return value * 2


x_map = custom_map(work, [1, 2, 5, 10])
print(next(x_map))
print(next(x_map))
print(next(x_map))
print(next(x_map))
print(list(custom_map(work, [1, 2, 5, 10])))


# Написать генератор, который бы работал как enumerate()
def custom_enumerate(some_iter, start=0):
    for i in some_iter:
        yield (start, i)
        start += 1


x_enumerate = custom_enumerate(['a', 'b', 'c'])
print(next(x_enumerate))
print(next(x_enumerate))
print(next(x_enumerate))

for i, v in custom_enumerate(['a', 'b', 'c', 'd']):
    print(i, ':', v)


# Написать генератор, который бы работал как zip()
def custom_zip(*iters):
    l_len = len(iters[0])

    for i in range(l_len):
        yield tuple(seq[i] for seq in iters)


s = 'abc'
t = (10, 20, 30)
u = (-5, -10, -15)

print(list(custom_zip(s, t, u)))
print(list(zip(s, t, u)))
