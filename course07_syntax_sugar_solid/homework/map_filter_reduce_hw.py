# ЗАДАЧИ НА MAP/FILTER/REDUCE (И LAMBDA, ЕСЛИ НУЖНО)

# 1. При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
from functools import reduce

print(list(map(lambda x: x % 5, [1, 4, 5, 30, 99])))

# 2. При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
print(list(map(str, [3, 4, 90, -2])))

# 3. При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
print(list(filter(lambda x: not isinstance(x, str), ['some', 1, 'v', 40, '3a', str])))

# 4. При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']
print(reduce(lambda a, b: a + b, list(map(len, ['some', 'other', 'value']))))
