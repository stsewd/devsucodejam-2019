# Arrange the pieces

# After putting a piece,
# a state can be:
# |0|0|x|
# |0|x|0|
#
# An especial case is when inserting a horizontal bar,
# but only another horizontal bar can be inserted in that case
# (filling 2 columns).
empty = 0
up = 1
down = 2

# After that state there are only a few options,
# and each option fills 1 or 2 columns.
rules = {
    empty: [(1, empty), (1, up), (1, down), (2, empty)],
    up: [(1, down), (2, empty)],
    down: [(1, up), (2, empty)],
}


def get_count(current_state, current_count):
    if current_count == 0 and current_state == empty:
        return 1
    if current_count <= 0:
        return 0

    total = sum(
        get_count(state, current_count - count) for count, state in rules[current_state]
    )
    return total


def solve(n):
    if n <= 0:
        return 0
    return get_count(empty, n)


def test():
    assert solve(0) == 0
    assert solve(1) == 1
    assert solve(2) == 2
    assert solve(3) == 5
    assert solve(4) == 11
