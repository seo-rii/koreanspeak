import hgtk

str = input()
lst = list()
for i in str:
    lst.append(hgtk.letter.decompose(i))

print(lst)
