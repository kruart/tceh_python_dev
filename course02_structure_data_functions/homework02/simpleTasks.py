# 1. create and sort list
import random

myList = [34, -3, 6, 0, 17, -79]
myList.sort()
print(myList)

# 2. create dict and print key/value
myDict = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth'}
for k, v in myDict.items():
    print(k, '-', v)

# 3. create tuple, find min and max in it
myTuple = (3, 48, 28, -27, -2, 0, 388, -21, 87, 11)
print('Min in tuple: ', min(myTuple))
print('Max in tuple: ', max(myTuple))

# 4. create list, and join all words in one with -> delimiter
joinList = ['Earth', 'Ukraine', 'Kyiv']
joinWord = ' -> '.join(joinList)
print(joinWord)

# 5. get str '/bin:/usr/bin:/usr/local/bin' and split it by ':' delimiter
splitStr = '/bin:/usr/bin:/usr/local/bin'.split(':')
print(splitStr)

# 6. go through all the numbers from 1 to 100, write to the console, which of them are divided into 7, and which are not
for i in range(0, 100):
    if i % 7 == 0:
        print(i, 'divided')
    else:
        print(i, 'not divided')

# 7. define matrix 3*4 and print all strs and all blocks
count = 0
matrix = [[random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)] for i in range(4)]
print(matrix)
print(matrix[1][2])

# 8. create list with any four objects and print object and his index in for loop
objectList = ['It\'s string', 1234, [23, -3232, 'str'], True]
for i in objectList:
    print(objectList.index(i), i)

# 9. create list with several 'to-delete' values and others, then delete all 'to-delete' values
removeFromList = ['first', 'to-delete', 'second', 'third', 'to-delete', 'someValue', 'someStr', 'to-delete']
print(removeFromList)
for i in removeFromList:
    if i == 'to-delete':
        removeFromList.remove(i)
print(removeFromList)


# iterate from 10 to 1
for i in range(10, 0, -1):
    print(i)