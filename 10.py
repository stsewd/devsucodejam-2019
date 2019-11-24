# Product subarray


def product(values):
    if not values:
        return values

    max_product = values[0]
    max_index = (0, 0)
    for i in range(len(values)):
        sub_product = 1
        for j in range(i, len(values)):
            sub_product *= values[j]
            if sub_product > max_product:
                max_product = sub_product
                max_index = (i, j)
    return values[max_index[0] : max_index[1] + 1]


def test():
    result = product([-3.2, 4.2, 7, 5.4, -2.2, -2.5])
    assert result == [-3.2, 4.2, 7, 5.4, -2.2]
