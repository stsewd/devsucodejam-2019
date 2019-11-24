# Pascal Triangle


def pascalTriangle(x, y):
    if y > x:
        return -1

    middle = x // 2
    if y > middle:
        y = x - y

    if y == 0:
        return 1

    row = [1]
    for i in range(x):
        extra = [] if i % 2 == 0 else [row[-1]]
        row = [a + b for a, b in zip(row + extra, [0] + row)]
    return row[y]


def test():
    assert pascalTriangle(2, 1) == 2
    assert pascalTriangle(1, 1) == 1
    assert pascalTriangle(0, 2) == -1
    assert pascalTriangle(50, 0) == 1
    assert pascalTriangle(6, 4) == 15
    assert pascalTriangle(7, 5) == 21
    assert pascalTriangle(8, 2) == 28
    assert pascalTriangle(8, 6) == 28
