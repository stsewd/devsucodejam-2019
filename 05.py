# Decrypt my message

import re

def decrypt(key, message):
    if not message:
        return ''
    key = key or 'DCJ'
    return re.sub(re.escape(key) + r'([AEIOUaeiou])', r'\1', message)


def test():
    result = decrypt('hi', 'hhiighhiEr hiordhiEr fhiUncthiihions')
    assert result == 'highEr ordEr fUnctions'

    result = decrypt('ll', 'hllalls')
    assert result == 'halls'

