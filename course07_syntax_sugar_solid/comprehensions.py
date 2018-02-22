#!/usr/bin/env python
# -*- coding: utf-8 -*-


s = [i for i in 'abcd']
print(s)
s = [w for w in range(1, 14)]
print(s)
s = [w for w in range(1, 14) if w % 2 == 0]
print(s)
s = [w for w in range(1, 14) if w % 2 != 0]
print(s)

words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

# very complex list comprehensions
l = [j for v in range(2, 5) for i in range(2, v) for j in range(i*2, 10, i)]
print(l)

# Dict comprehensions
country = ['India', 'Pakistan', 'Nepal', 'Bhutan', 'China', 'Bangladesh']
capital = ['New Delhi', 'Islamabad','Kathmandu', 'Thimphu', 'Beijing', 'Dhaka']

print({country[i]: capital[i] for i in range(len(country))})
