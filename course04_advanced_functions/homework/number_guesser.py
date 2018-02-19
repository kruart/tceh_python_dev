import random


def main():
    number = random.randint(1, 100)
    while True:
        try:
            guess_number = int(input())

            if guess_number == number:
                print('Correct!!!')
                break
            elif guess_number < number:
                print('Too low')
            elif guess_number > number:
                print('Too high')
        except ValueError as err:
            print('incorrect data')


if __name__ == '__main__':
        # See what this means: http://stackoverflow.com/questions/419163/what-does-if-name-main-do
        main()
        print("End of program.")