fin = open("milkorder.in")
n, m, k = map(int, fin.readline().split())
hier = map(int, fin.readline().split())
ordi = []
orli = []

mlist = [0 for i in range(n + 1)]
for i in range(k):
    #print(i)
    f = map(int, fin.readline().split())
    ordi.append(f[0])
    orli.append(f[1])
    mlist[f[1]] = f[0]

print(hier)
print(ordi)
print(orli)

hior = list(set(ordi).intersection(set(hier)))
mlist[0] = "x"

if len(hior) > 0:
    s = orli[ordi.index(hior[0])]
    h = hier.index(hior[0])
    c = 0
else:
    s = len(mlist)
    h = len(hior) - 1
    c = len(hier) - s
for i in range(s - 1, 0, -1):
    if c < 0:
        break
    print(mlist)
    print(h, s, c, i)
    if mlist[i] == 0:
        mlist[i] = hier[h - c - 1]
    else:
        c -= 1
print(mlist)

fout = open("milkorder.out", "w")
fout.write(str(mlist.index(0)) + "\n")
fout.close()
