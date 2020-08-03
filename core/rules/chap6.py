import rules.chardetect as charD
import rules.charproc as charP


def rule23(a, b, c, p, q, r):
    if charD.isTypeOfㄱ(c) or charD.isTypeOfㄷ(c) or charD.isTypeOfㅂ(c):
        p = charP.toHard(p)
    return a, b, c, p, q, r
