# Minesweeper map

def count_bombs(i, j, board):
    len_x = len(board)
    len_y = len(board[i])

    bombs = 0
    # 1 2 3
    # 4 x 6
    # 7 8 9

    for m in range(3):
        x = i - 1 + m
        y = j - 1
        if 0 <= x < len_x:
            for n in range(3):
                if 0 <= y + n < len_y:
                    if board[x][y + n] == 'x':
                        bombs += 1
    return bombs


def minesweeper(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'x':
                board[i][j] = str(count_bombs(i, j, board))
    return board


def test():
    input = [
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' '],
        [' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
        [' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x'],
        [' ', 'x', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' '],
    ]
    expected = [
        ['0', '1', '2', 'x', '2', '1', '2', 'x', '2', '1'],
        ['1', '2', 'x', '2', '3', 'x', '5', '4', '4', 'x'],
        ['1', 'x', '3', '2', '4', 'x', 'x', 'x', 'x', '2'],
        ['1', '1', '2', 'x', '4', 'x', '8', 'x', '5', '2'],
        ['1', '1', '2', '2', '5', 'x', 'x', 'x', '3', 'x'],
        ['1', 'x', '1', '1', 'x', 'x', 'x', '3', '2', '1'],
    ]
    assert minesweeper(input) == expected
