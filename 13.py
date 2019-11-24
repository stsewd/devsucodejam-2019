# Toeplitz matrix


def solve(matrix):
    unique = set()
    len_x = len(matrix)
    len_y = len(matrix[0])
    lim = min(len_y, len_x)

    # Upper
    for i in range(len_y):
        n = matrix[0][i]
        max_x = min(len_y - i, lim)
        for j in range(max_x):
            if matrix[j][i + j] != n:
                return -1
        unique.add(n)

    # Lower
    for i in range(1, len_x):
        n = matrix[i][0]
        max_x = min(len_x - i, lim)
        for j in range(max_x):
            if matrix[i + j][j] != n:
                return -1
        unique.add(n)

    return len(unique)


def test():
    matrix = [
        [1, 2, 3, 4, 8, 1],
        [5, 1, 2, 3, 4, 8],
        [4, 5, 1, 2, 3, 4],
        [7, 4, 5, 1, 2, 3],
    ]
    assert solve(matrix) == 7

    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [4, 5, 1, 2],
        [7, 4, 5, 1],
        [7, 7, 4, 5],
        [7, 7, 7, 4],
    ]
    assert solve(matrix) == 6

    matrix = [
        [1, 2],
        [5, 1],
        [4, 5],
    ]
    assert solve(matrix) == 4

    matrix = [
        [1, 2],
        [5, 5],
        [4, 5],
    ]
    assert solve(matrix) == -1
