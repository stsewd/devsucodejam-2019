# Track my time
def track(times):
    if not times:
        return [0, 0, 0, 0, 0]
    ms = 0
    for t in times:
        if t < 0:
            continue
        ms += t
    miliseconds = (ms) % 1000
    seconds = (ms/1000) % 60
    minutes = (ms/(1000 * 60)) % 60
    hours = (ms/(1000 * 60 * 60)) % 24
    days = (ms/(1000 * 60 * 60 * 24))
    return [int(days), int(hours), int(minutes), int(seconds), int(miliseconds)]


def test():
    result = track([65647440, 199644521])
    assert result == [3, 1, 41, 31, 961]
