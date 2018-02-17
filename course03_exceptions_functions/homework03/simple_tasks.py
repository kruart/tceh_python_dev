# try/except
# 1. input a number, if number is even throws ValueError, if odd - TypeError. Then handle error
try:
    number = int(input('Input a number'))
    if number % 2 == 0:
        raise ValueError
    elif number < 0:
        raise TypeError
    elif number > 10:
        raise IndexError
except ValueError as err:
    print('number is even')
except TypeError as err:
    print('number is less 0')
except IndexError as err:
    print('number is bigger than 10')



# 2. create a list, get item by index, and handle possible error if item doesn't exist by index
myList = [32, 'str', True, [2, -32, 0], -2378, 'value', 'footballClub']
try:
    index = int(input('Input an item index'))
    print(myList[index])
except IndexError as err:
    print('Error!', err)


# functions
# 1. write functions with two args. If both args > than 0, return its sum. If both args < 0, return difference. If one > 0, and one < 0, return 0
def get_numbers(a: int, b: int) -> int:
    if a > 0 and b > 0:
        return a + b
    elif a < 0 and b < 0:
        return a - b
    else:
        return 0


print(get_numbers(10, 9))
print(get_numbers(-10, -9))
print(get_numbers(10, -9))


# 2. Write a function that takes 3 arguments - numbers, find two maximal ones among them, output to the console
def print_two_max_numbers(a: int, b: int, c: int) -> None:
    print(*sorted([a, b, c])[-2::])


print_two_max_numbers(2, 33, -3)


# 3. Write a function that takes two arguments. The first is a list of numbers, the second is a boolean flag.
# If the flag is valid - return a new list with odd numbers from the input list,
# if the flag is negative - return a new list with even numbers from the input list
def get_sub_list(someList: list, flag: bool) -> list:
    if flag:
        return list(filter(lambda i: i % 2 != 0, someList))
    else:
        return list(filter(lambda i: i % 2 == 0, someList))


print(get_sub_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False))


# *args, **kwargs
# 1. Write a function that takes any number of argument numbers. Among them, it finds the max and min. And returns both
def find_min_max(*args: int) -> list:
    return [min(args), max(args)]


print(find_min_max(38, 9, -3, -38, 12, 77, -12))


# 2. Write a function that takes two arguments: the string and the boolean case flag is set to True by default.
# If the flag is valid: return a new line, where each character is upper case, otherwise - to the bottom
def return_new_line(some_str: str, case=True) -> str:
    if case:
        return some_str.upper()
    else:
        return some_str.lower()


print(return_new_line('Some String'))
print(return_new_line('Some String', False))


# 3. Write a function that takes any number of positional arguments - strings and one default glue, which is equal to ':'.
# Join all the lines in such a way that the result is all the lines, longer than 3 characters. To Join between any two lines, insert a glue
def join_args(*args, glue=':') -> str:
    myList = []
    for i in args:
        if len(i) > 3:
            myList.append(i)
    return glue.join(myList)

print(join_args('some', 'value', 'with', 'glue'))