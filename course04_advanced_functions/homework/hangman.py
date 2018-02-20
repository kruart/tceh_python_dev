import random
from collections import OrderedDict

WORDS = ['python', 'language', 'microservices', 'architecture', 'context', 'pattern', 'application']
MAX_ERRORS = 7


def get_random_word() -> str:
    return random.choice(WORDS)


def get_initial_statuses(word: str) -> list:
    statuses = []
    for i in word:
        statuses.append(False)
    return statuses


def check_letter(word: str, letter: str, statuses: list) -> bool:
    if letter not in word:
        return False

    for index, ch in enumerate(word):
        if letter == ch:
            statuses[index] = True

    return True


def print_word(word: str, statuses: list) -> None:
    for index, letter in enumerate(word):
        if not statuses[index]:
            print('_', end=' ')
        else:
            print(letter, end=' ')


def user_input() -> str:
    while True:
        letter = str(input(''))
        if len(letter) == 1:
            return letter
        else:
            print('input ONLY ONE letter')


def is_game_finished(current_err: int, statuses: list) -> bool:
    if current_err >= MAX_ERRORS or all(v is True for v in statuses):
        return True
    else:
        return False


def main():
    current_errors = 0
    word = get_random_word()
    statuses = get_initial_statuses(word)

    while not is_game_finished(current_errors, statuses):
        print_word(word, statuses)
        s = user_input()
        result = check_letter(word, s, statuses)

        if not result:
            current_errors += 1

    if current_errors >= MAX_ERRORS:
        print('You lose!')
    else:
        print_word(word, statuses)
        print('\nYou won!')


if __name__ == '__main__':
    # See what this means: http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
    print("End of program.")
