# Nth case


def nthCase(n, message):
    if not message:
        return ""
    if n <= 0:
        return message
    result = list(message)
    for i in range(n - 1, len(message), n):
        w = result[i]
        result[i] = w.upper() if w.islower() else w.lower()
    return "".join(result)


def test():
    result = nthCase(3, "Greetings, this is AN EXAMPLE!")
    assert result == "GrEetIngS, ThiS iS An ExAMpLE!"
