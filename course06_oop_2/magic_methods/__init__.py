# -*- coding: utf-8 -*-
class MathObject(object):
    def __init__(self):
        self.value = 2

    def __add__(self, other):
        return self.value + other


t = MathObject()
print(t + 4)
print(t.__add__(4))