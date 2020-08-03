import rules.chardetect as charD


def rule17(a, b, c, p, q, r):
    if p == 'ㅇ' and q == 'ㅣ':
        if c == 'ㄷ':
            c = ''
            p = 'ㅈ'
        elif c == 'ㅌ' or c == 'ㄾ':
            c = ''
            p = 'ㅊ'
    return a, b, c, p, q, r


def rule18(a, b, c, p, q, r):
    if p == 'ㄴ' or p == 'ㅁ':
        if charD.isTypeOfㄱ(c):
            c = 'ㅇ'
        elif charD.isTypeOfㄷ(c) or c == 'ㅎ':
            c = 'ㄴ'
        elif charD.isTypeOfㅂ(c):
            c = 'ㅁ'
    return a, b, c, p, q, r


def rule19(a, b, c, p, q, r):
    if c == 'ㅁ' or c == 'ㅇ':
        if p == 'ㄹ':
            p = 'ㄴ'
    return a, b, c, p, q, r


def rule20(a, b, c, p, q, r):
    if c == 'ㄴ' and p == 'ㄹ':
        c = 'ㄹ'
    elif (c == 'ㄹ' or c == 'ㄾ' or c == 'ㅀ') and p == 'ㄴ':
        p = 'ㄹ'
    return a, b, c, p, q, r
