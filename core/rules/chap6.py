import rules.chardetect as charD
import rules.charproc as charP


def rule23(a, b, c, p, q, r):
    if charD.isTypeOfㄱ(c) or charD.isTypeOfㄷ(c) or charD.isTypeOfㅂ(c):
        p = charP.toHard(p)
    return a, b, c, p, q, r


def rule24(a, b, c, p, q, r):
    if c == 'ㄴ' or c == 'ㄵ' or c == 'ㅁ' or c == 'ㄻ':
        if p == 'ㄱ' or p == 'ㄷ' or p == 'ㅅ' or p == 'ㅈ':
            p = charP.toHard(p)
    return a, b, c, p, q, r


def rule25(a, b, c, p, q, r):
    if c == 'ㄼ' or c == 'ㄾ':
        if p == 'ㄱ' or p == 'ㄷ' or p == 'ㅅ' or p == 'ㅈ':
            p = charP.toHard(p)
    return a, b, c, p, q, r
