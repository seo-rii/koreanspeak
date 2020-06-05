import hgtk
import rules.chap4 as chap4

str = input()
lst = list()
res = ""

for i in str:
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

        (a, b, c, p, q, r) = chap4.rule16(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule15(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule13(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule14(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule9(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule10(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule11(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule12(a, b, c, p, q, r)

        lst[i][1] = [a, b, c]
        lst[i + 1][1] = [p, q, r]

lst.pop()

for i in lst:
    if i[0]:
        res += hgtk.letter.compose(i[1][0], i[1][1], i[1][2])
    else:
        res += i[1]

print(res)
