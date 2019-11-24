# Clock Angles

import re


def angles(times):
    total = 0
    pattern = re.compile(r"([0-2][0-9]):([0-5][0-9])")
    for time in times:
        match = pattern.match(time)
        if not match:
            total -= 100
            continue
        h, m = map(int, match.groups())
        if not (0 <= h < 24):
            total -= 100
            continue
        if not (0 <= m < 60):
            total -= 100
            continue

        h = (h % 12) + (m * (1 / 60))
        m = m / 5
        if h <= m:
            total += (m - h) * 30
        else:
            total += (12 - (h - m)) * 30
    return total


import pytest


def test():
    result = angles(["12:00", "17:30", "blabla", "20:21", "26:88"])
    assert result == pytest.approx(50.5)
