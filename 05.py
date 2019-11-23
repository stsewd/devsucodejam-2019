# Decrypt my message

import re

def decrypt(key, message):
    if not message:
        return ''
    key = key or 'DCJ'
    return re.sub(re.escape(key) + r'([AEIOUaeiou])', r'\1', message)
