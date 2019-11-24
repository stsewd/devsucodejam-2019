# Distinct characters

def solve(message):
    if not message:
        return 0

    message = message.lower()
    unique = set(message)
    min_len = len(unique)
    len_message = len(message)
    if len_message == min_len:
        return min_len

    min_result = len_message
    for i in range(len_message - min_len):
        for j in range(i + min_len, len_message + 1):
            superset = set(message[i:j])
            if unique.issubset(superset):
                min_result = min(min_result, j - i)
    return min_result


def test():
    assert solve('gamer programming') == 13
    assert solve('uniqe') == 5
    assert solve('unique') == 6
