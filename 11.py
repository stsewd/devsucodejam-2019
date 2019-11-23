# Pascal Triangle

def pascalTriangle(x, y):
    """
    Hack para dar una solución rápida,
    sólo funciona hasta la columna 4.
    """
    row = 11 ** x
    col = str(row)[-(y + 1)]
    return int(col)


def test():
    assert pascalTriangle(2, 1) == 2
    # TODO
    # assert pascalTriangle(6, 4) == 15
