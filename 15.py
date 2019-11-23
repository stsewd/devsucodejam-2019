# Kaprekar’s Cons

def solve(n):
    magic = 6174
    steps = 0
    numbers = n
    while True:
        steps += 1
        numbers = str(numbers)
        if len(set(numbers)) < 2:
            return -1
        if len(numbers) > 4:
            return -1

        max_ = sorted(numbers, reverse=True)
        min_ = list(reversed(max_))
        max_ = int(''.join(max_))
        min_ = int(''.join(min_))
        numbers = max_ - min_
        if numbers == magic:
            return steps
