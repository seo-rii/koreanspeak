import rules.chardetect as char


def rule9(a, b, c, p, q, r):
    if c == 'ㅋ' or c == 'ㄲ':
        c = 'ㄱ'
    if c == 'ㅅ' or c == 'ㅆ' or c == 'ㅈ' or c == 'ㅊ' or c == 'ㅌ':
        c = 'ㄷ'
    if c == 'ㅍ':
        c = 'ㅂ'
    return (a, b, c, p, q, r)


def rule10(a, b, c, p, q, r):
    if c == 'ㄳ':
        c = 'ㄱ'
    if c == 'ㄵ':
        c = 'ㄴ'
    if c == 'ㄼ' or c == 'ㄽ' or c == 'ㄾ':
        if c == 'ㄼ' and (not (p == 'ㅇ') and p):
            c = 'ㅂ'
        else:
            c = 'ㄹ'
    if c == 'ㅄ':
        c = 'ㅂ'
    return (a, b, c, p, q, r)


def rule11(a, b, c, p, q, r):
    if c == 'ㄺ':
        if p == 'ㄱ':
            c = 'ㄹ'
        else:
            c = 'ㄱ'
    if c == 'ㄻ':
        c = 'ㅁ'
    if c == 'ㄿ':
        c = 'ㅂ'
    return (a, b, c, p, q, r)


def rule12(a, b, c, p, q, r):
    if c == 'ㅎ' or c == 'ㅀ' or c == 'ㄶ':
        if p == 'ㄱ':
            p = 'ㅋ'
            if c == 'ㅀ':
                c = 'ㄹ'
            elif c == 'ㄶ':
                c = 'ㄴ'
            else:
                c = ''
        elif p == 'ㄷ':
            p = 'ㅌ'
            if c == 'ㅀ':
                c = 'ㄹ'
            elif c == 'ㄶ':
                c = 'ㄴ'
            else:
                c = ''
        elif p == 'ㅈ':
            p = 'ㅊ'
            if c == 'ㅀ':
                c = 'ㄹ'
            elif c == 'ㄶ':
                c = 'ㄴ'
            else:
                c = ''
        elif p == 'ㅅ':
            p = 'ㅆ'
            if c == 'ㅀ':
                c = 'ㄹ'
            elif c == 'ㄶ':
                c = 'ㄴ'
            else:
                c = ''
        elif p == 'ㄴ':
            if c == 'ㅀ':
                c = 'ㄹ'
            elif c == 'ㄶ':
                c = 'ㄴ'
            else:
                c = 'ㄴ'
        elif p == 'ㅇ':
            if c == 'ㅀ':
                p = 'ㄹ'
            elif c == 'ㄶ':
                p = 'ㄴ'
            c = ''
    if p == 'ㅎ':
        if c == 'ㄱ':
            p = 'ㅋ'
            c = ''
        elif c == 'ㄷ':
            p = 'ㅌ'
            c = ''
        elif c == 'ㅈ':
            p = 'ㅊ'
            c = ''
    return (a, b, c, p, q, r)


def rule13(a, b, c, p, q, r):
    if c not in char.gyeop_consonant:
        if p == 'ㅇ':
            if c and c != 'ㅎ':
                p = c
                c = ''
    return (a, b, c, p, q, r)


def rule14(a, b, c, p, q, r):
    if c in char.gyeop_consonant:
        if p == 'ㅇ':
            (c, p) = char.gyeop_consonant[c]
            if p == 'ㅅ':
                p = 'ㅆ'
    return (a, b, c, p, q, r)
