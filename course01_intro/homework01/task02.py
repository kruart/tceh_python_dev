# 1. find Area of a Rectangle
width = float(input('Please Enter the Width of a Rectangle'))
height = float(input('Please Enter the Height of a Rectangle'))

area = width * height
print('Area of a Rectangle is: {}'.format(area))


# 2. asks the user for two numbers and the sign: "+" or "-". Depending on the sign displays their sum or difference
numberOne = float(input('Enter number one: '))
numberTwo = float(input('Enter number two: '))
sign = input('Enter the sign + or -: ')

answer = (numberOne + numberTwo) if sign == '+' else numberOne - numberTwo
print(answer)


# 3. found if number is prime
someNumber = int(input('Enter number: '))

if someNumber > 1:
    for i in range(2, someNumber):
        if (someNumber % i) == 0:
            print(someNumber, "is not a prime number.")
            break
    else:
        print(someNumber, 'is a prime number.')
else:
    print(someNumber, 'is not a prime number.')


# 4. displays all the multiple 5 numbers between two user numbers
numberOne = int(input('Enter number one: '))
numberTwo = int(input('Enter number two: '))

for i in range(numberOne, numberTwo + 1):
    if i % 5 == 0:
        print(i)


