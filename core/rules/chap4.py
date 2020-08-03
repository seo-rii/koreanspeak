import rules.chardetect as charD
import rules.charproc as charP


def rule9(a, b, c, p, q, r):
    if c == 'ㅋ' or c == 'ㄲ':
        c = 'ㄱ'
    if charD.isTypeOfㄷ(c):
        c = 'ㄷ'
    if c == 'ㅍ':
        c = 'ㅂ'
    return a, b, c, p, q, r


def rule10(a, b, c, p, q, r):
    if c == 'ㄳ':
        c = 'ㄱ'
    if c == 'ㄵ':
        c = 'ㄴ'
    if c == 'ㄼ' or c == 'ㄽ' or c == 'ㄾ':
        c = 'ㄹ'
    if c == 'ㅄ':
        c = 'ㅂ'
    return a, b, c, p, q, r


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
    return a, b, c, p, q, r


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
        if c == 'ㄱ' or c == 'ㄷ' or c == 'ㅈ':
            p = charP.toStrong(c)
            c = ''
    return a, b, c, p, q, r


def rule13(a, b, c, p, q, r):
    if c not in charD.gyeop_consonant:
        if p == 'ㅇ':
            if c and c != 'ㅎ':
                p = c
                c = ''
    return a, b, c, p, q, r


def rule14(a, b, c, p, q, r):
    if c in charD.gyeop_consonant:
        if p == 'ㅇ':
            (c, p) = charD.gyeop_consonant[c]
            if p == 'ㅅ':
                p = 'ㅆ'
    return a, b, c, p, q, r


def rule15(a, b, c, p, q, r):
    if p == 'ㅇ':
        if q == 'ㅏ' or q == 'ㅓ' or q == 'ㅗ' or q == 'ㅜ' or q == 'ㅟ':
            (a, b, c, p, q, r) = rule9(a, b, c, p, q, r)
            (a, b, c, p, q, r) = rule10(a, b, c, p, q, r)
            (a, b, c, p, q, r) = rule11(a, b, c, p, q, r)
            (a, b, c, p, q, r) = rule12(a, b, c, p, q, r)
            if c:
                p = c
                c = ''
    return a, b, c, p, q, r


def rule16(a, b, c, p, q, r):
    if p == 'ㅇ':
        if q == 'ㅣ' or q == 'ㅡ' or q == 'ㅔ':
            if c == 'ㄷ' or c == 'ㅈ' or c == 'ㅊ' or c == 'ㅌ' or c == 'ㅎ':
                p = 'ㅅ'
                c = ''
            if c == 'ㅋ':
                p = 'ㄱ'
                c = ''
            if c == 'ㅍ':
                p = 'ㅂ'
                c = ''
    return a, b, c, p, q, r
