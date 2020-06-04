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

if len(lst) == 1:
    a = lst[0][1][0]
    b = lst[0][1][1]
    c = lst[0][1][2]
    (a, b, c) = chap4.rule9(a, b, c, None, None, None)
    (a, b, c) = chap4.rule10(a, b, c, None, None, None)
    (a, b, c) = chap4.rule11(a, b, c, None, None, None)
    lst[0][1][0] = a
    lst[0][1][1] = b
    lst[0][1][2] = c

for i in range(len(lst) - 1):
    if lst[i][0]:
        a = lst[i][1][0]
        b = lst[i][1][1]
        c = lst[i][1][2]
        if lst[i + 1][0]:
            p = lst[i + 1][1][0]
            q = lst[i + 1][1][1]
            r = lst[i + 1][1][2]
        else:
            p = False
            q = False
            r = False

        (a, b, c, p, q, r) = chap4.rule13(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule14(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule9(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule10(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule11(a, b, c, p, q, r)
        (a, b, c, p, q, r) = chap4.rule12(a, b, c, p, q, r)

        lst[i][1][0] = a
        lst[i][1][1] = b
        lst[i][1][2] = c
        lst[i + 1][1][0] = p
        lst[i + 1][1][1] = q
        lst[i + 1][1][2] = r

for i in lst:
    if i[0]:
        res += hgtk.letter.compose(i[1][0], i[1][1], i[1][2])
    else:
        res += i[1]

print(res)
