board_cells = list(range(1, 11))
X_MARK = 'X'
O_MARK = 'O'


def print_board(cells: list) -> None:
    print('+-------+-------+-------+')
    print('|\t{}\t|\t{}\t|\t{}\t|'.format(cells[0], cells[1], cells[2]))
    print('+-------+-------+-------+')
    print('|\t{}\t|\t{}\t|\t{}\t|'.format(cells[3], cells[4], cells[5]))
    print('+-------+-------+-------+')
    print('|\t{}\t|\t{}\t|\t{}\t|'.format(cells[6], cells[7], cells[8]))
    print('+-------+-------+-------+')


def check_cell(cell: int, cells: list) -> bool:
    return cells[cell - 1] == cell


def user_input() -> int:
    while True:
        try:
            num = int(input(''))
            if 1 <= num <= 9:
                return num
            else:
                raise ValueError
        except ValueError:
            print('Input a number from 1 to 9\n')
        except TypeError:
            print('Input a number from 1 to 9\n')


def is_winner_exists(cells: list) -> str:
    WAYS_WIN = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    )

    for line in WAYS_WIN:
        if all(cells[cell] == X_MARK for cell in line):
            return 'X won'
        elif all(cells[cell] == O_MARK for cell in line):
            return 'O won'

    for line in WAYS_WIN:
        # if empty cell still exist
        if any(cell + 1 == cells[cell] for cell in line):
            return ''
    return 'Drawn'


def is_game_finished(cells: list) -> bool:
    return is_winner_exists(cells) != ''


def do_mark(cell_index, cells, mark):
    cells[cell_index - 1] = mark


def main():
    is_x_moves = True

    while not is_game_finished(board_cells):
        print_board(board_cells)
        cell_index = user_input()
        is_cell_free = check_cell(cell_index, board_cells)

        if is_cell_free:
            if is_x_moves:
                do_mark(cell_index, board_cells, X_MARK)
                is_x_moves = False
            else:
                do_mark(cell_index, board_cells, O_MARK)
                is_x_moves = True

    print_board(board_cells)
    print(is_winner_exists(board_cells))


if __name__ == '__main__':
    main()
