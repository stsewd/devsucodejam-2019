# Product subarray

import itertools

def product(values):
    if not values:
        return values

    max_ = values[0]
    max_index = (0, 0)
    for i in range(len(values)):
        sub_sum = 1
        for j in range(i, len(values)):
            sub_sum *= values[j]
            if sub_sum > max_:
                max_ = sub_sum
                max_index = (i, j)
    return values[max_index[0]:max_index[1] + 1]


def test():
    result = product([-3.2, 4.2, 7, 5.4, -2.2, -2.5])
    assert result == [-3.2, 4.2, 7, 5.4, -2.2]
