# Series reloaded

def series(n):
    if n <= 0:
        return -1
    seed = -3
    for i in range(n - 1):
        seed += ((i + 1) * 2) - 1
    return seed


def test():
    serie = [-3, -2, 1, 6, 13, 22, 33, 46, 61, 78]
    for i, n in enumerate(serie, start=1):
        assert n == series(i)
