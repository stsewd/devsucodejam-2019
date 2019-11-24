# Encrypt your message


def encrypt(key, message):
    if not message:
        return ""
    key = key or "DCJ"

    solution = ""
    vowels = {"a", "e", "i", "o", "u"}
    for m in message:
        if m.lower() in vowels:
            solution += key
        solution += m
    return solution


def test():
    result = encrypt("dcj", "I love prOgrAmming!")
    assert result == "dcjI ldcjovdcje prdcjOgrdcjAmmdcjing!"
