import hgtk
import rules.chap4 as chap4
import rules.chap5 as chap5
import rules.chap6 as chap6

query = input()
lst = list()
res = ""

for i in query:
    if hgtk.checker.is_hangul(i):
        lst.append([True, list(hgtk.letter.decompose(i))])
    else:
        lst.append([False, i])

lst.append([False, ''])

for i in range(len(lst) - 1):
    if lst[i][0]:
        (a, b, c) = lst[i][1]
        if lst[i + 1][0]:
            (p, q, r) = lst[i + 1][1]
        else:
            p = False
            q = False
            r = False

        (a, b, c, p, q, r) = chap5.rule17(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap5.rule20(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap6.rule24(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap6.rule25(a, b, c, p, q, r)

        (a, b, c, p, q, r) = chap4.rule16(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule15(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule13(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule14(a, b, c, p, q, r)

        (a, b, c, p, q, r) = chap5.rule18(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap5.rule19(a, b, c, p, q, r)

        (a, b, c, p, q, r) = chap4.rule9(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule10(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule11(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule12(a, b, c, p, q, r)

        (a, b, c, p, q, r) = chap6.rule23(a, b, c, p, q, r)

        lst[i][1] = [a, b, c]
        lst[i + 1][1] = [p, q, r]

lst.pop()

for i in lst:
    if i[0]:
        res += hgtk.letter.compose(i[1][0], i[1][1], i[1][2])
    else:
        res += i[1]

print(res)
