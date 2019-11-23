# Sum to zero

import itertools

def short(values):
    for i in range(len(values)):
        sub_sum = 0
        for j in range(i, len(values)):
            sub_sum += values[j]
            if sub_sum == 0:
                return values[:i] + values[j + 1:]
    return values

def solve(values):
    if not values:
        return []
    while True:
        new_values = short(values)
        if not new_values or new_values == values:
            return new_values
        values = new_values
    return values


def test():
    assert solve([3, 4, -7, 5, -6, 2, 5, -1, 8]) == [5, 8]
