def toStrong(c):
    if c == 'ㄱ':
        c = 'ㅋ'
    if c == 'ㄷ':
        c = 'ㅌ'
    if c == 'ㅂ':
        c = 'ㅍ'
    if c == 'ㅈ':
        c = 'ㅊ'
    return c


def toHard(c):
    if c == 'ㄱ':
        c = 'ㄲ'
    if c == 'ㄷ':
        c = 'ㄸ'
    if c == 'ㅂ':
        c = 'ㅃ'
    if c == 'ㅅ':
        c = 'ㅆ'
    if c == 'ㅈ':
        c = 'ㅉ'
    return c


def toNatural(c):
    if c == 'ㅋ' or c == 'ㄲ':
        c = 'ㄱ'
    if c == 'ㅌ' or c == 'ㄸ':
        c = 'ㄷ'
    if c == 'ㅍ' or c == 'ㅃ':
        c = 'ㅂ'
    if c == 'ㅆ':
        c = 'ㅅ'
    if c == 'ㅊ' or c == 'ㅉ':
        c = 'ㅈ'
    return c
