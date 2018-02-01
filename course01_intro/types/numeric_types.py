# ints:
print('int------------------------')
print('1 + 2 = ', 1 + 2)
print('5 * 9 = ', 5 * 9)

# floats:
print('float------------------------')
print('1.3 * 0.3 = ', 1.3 * 0.3)
print('1.3 * .3 = ', 1.3 * .3)
print('279 * .105 = ', 279 * .105)

# mixed:
print('mixed------------------------')
print('1 + 1.5 = ', 1 + 1.5)
print('3 * 0.5 = ', 3 * 0.5)

# complex:
print('complex------------------------')
print('1j * 1j = ', 1j * 1j)  # 1j = sqrt(-1)



# operations priority
print('priority------------------------')
print('2 + 2 * 2 = ', 2 + 2 * 2)
print('(2 + 2) * 2 = ', (2 + 2) * 2)    # use whitespace
print('(2+2)*2 = ', (2+2)*2)            # ugly and unreadable way to write code

# with whitespace in the beginning
"""
>>> 1 + 1
"""




# overfloating int:
import sys  # importing the standard library `sys`.
print('------------------------')
print('sys.maxsize = ', sys.maxsize)

print('sys.maxsize + 1 = ', sys.maxsize + 1)

print('-sys.maxsize = ', -sys.maxsize)
print('-sys.maxsize - 1 = ', -sys.maxsize - 1)
print('-sys.maxsize - 2 = ', -sys.maxsize - 2)


# # division:
print('------------------------')
print('4 / 3 = ', 4 / 3)
