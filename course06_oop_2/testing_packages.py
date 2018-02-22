# -*- coding: utf-8 -*-


from course06_oop_2.normal_package.normal_file import MyClass, my_function, GLOBAL_VAR, special_function


my_function()
special_function()


print("__name__ in testing_package.py", __name__)

try:
    from not_a_package.my_module import print_info

    # why does it happen:
    # http://stackoverflow.com/questions/16981921/relative-imports-in-python-3
    print_info()
except ImportError as e:
    print(e)



