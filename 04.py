# Series reloaded

def series(n):
    if n <= 0:
        return -1
    seed = -3
    for i in range(n - 1):
        seed += ((i + 1) * 2) - 1
    return seed
