import random

EMPTY_MARK = 'X'
puzzles = list(range(1, 16))
puzzles.append(EMPTY_MARK)
answer = str(puzzles).strip('[]')
random.shuffle(puzzles)


def main():
    count_moves = 0
    try:
        while True:
            x_pos = puzzles.index(EMPTY_MARK)
            print_board(puzzles)
            user_move = input('your move w,a,s,d\n')
            is_right_move = check_move(x_pos, user_move)
            if is_right_move:
                do_move(user_move, x_pos)
                count_moves += 1
            else:
                print('Wrong move')

            if str(puzzles).strip('[]') == answer:
                print('You won in', count_moves, 'moves! Congratulate!')
                break
    except KeyboardInterrupt:
        print('shutting down')


def print_board(puzzle_list: list) -> None:
    print('+-------+-------+-------+-------+')
    print('|\t%s\t|\t%s\t|\t%s\t|\t%s\t|' % (puzzle_list[0], puzzle_list[1], puzzle_list[2], puzzle_list[3]))
    print('+-------+-------+-------+-------+')
    print('|\t%s\t|\t%s\t|\t%s\t|\t%s\t|' % (puzzle_list[4], puzzle_list[5], puzzle_list[6], puzzle_list[7]))
    print('+-------+-------+-------+-------+')
    print('|\t%s\t|\t%s\t|\t%s\t|\t%s\t|' % (puzzle_list[8], puzzle_list[9], puzzle_list[10], puzzle_list[11]))
    print('+-------+-------+-------+-------+')
    print('|\t%s\t|\t%s\t|\t%s\t|\t%s\t|' % (puzzle_list[12], puzzle_list[13], puzzle_list[14], puzzle_list[15]))
    print('+-------+-------+-------+-------+')


def check_move(x_pos: int, move: str) -> bool:
    if move == 'w' and all([i != x_pos for i in range(0, 4)]):
        return True
    elif move == 's' and all([i != x_pos for i in range(12, 16)]):
        return True
    elif move == 'a' and all(i != x_pos for i in [0, 4, 8, 12]):
        return True
    elif move == 'd' and all(i != x_pos for i in [3, 7, 11, 15]):
        return True

    return False


def do_move(user_move, x_pos):
    if user_move == 'w':
        puzzles[x_pos - 4], puzzles[x_pos] = puzzles[x_pos], puzzles[x_pos - 4]
    elif user_move == 's':
        puzzles[x_pos + 4], puzzles[x_pos] = puzzles[x_pos], puzzles[x_pos + 4]
    elif user_move == 'a':
        puzzles[x_pos - 1], puzzles[x_pos] = puzzles[x_pos], puzzles[x_pos - 1]
    elif user_move == 'd':
        puzzles[x_pos + 1], puzzles[x_pos] = puzzles[x_pos], puzzles[x_pos + 1]


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
