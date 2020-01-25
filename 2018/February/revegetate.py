fin = open("revegetate.in", "r")
n, m = map(int, fin.readline().split())
pasli = [0 for i in range(n + 1)]
samed = set()
diffed = set()
diffdiff = set()
samsam = set()
prefli = []
samli = []
for i in range(m):
    lin = fin.readline().split()
    if lin[0] == "S":
        samli.append(lin)
        """if lin[1] in samed and lin[2] not in samed:
            pasli[int(lin[2])] = pasli[int(lin[1])]
            samed.update(lin[1:])
        elif lin[1] not in samed and lin[2] in samed:
            pasli[int(lin[1])] = pasli[int(lin[1])]
            samed.update(lin[1:])
        else:

        pasli[int(lin[1])] = 1
        pasli[int(lin[2])] = 1
        samed.update(lin[1:])"""
    else:
        prefli.append(lin)
        #diffed.update(lin[1:])
print(samli)
print(prefli)
r = 1
for item in samli:
    print(item)
    if pasli[int(lin[1])] == 0 and pasli[int(lin[2])] == 0:
        print("new")
        pasli[int(lin[1])] = r
        pasli[int(lin[2])] = r
        r += 1
    else:
        pasli[int(lin[1])] = max(pasli[int(lin[1])], pasli[int(lin[2])])
        pasli[int(lin[2])] = max(pasli[int(lin[1])], pasli[int(lin[2])])
    print pasli

"""inters = 0
poss = 1
for lin in prefli:
    if lin[1] in samed and lin[2] not in samed:
        pasli[int(lin[2])] = 2
        inters += 1
    elif lin[2] in samed and lin[1] not in samed:
        pasli[int(lin[1])] = 2
        inters += 1
    elif lin[2] in samed and lin[1] in samed:
        poss = 0
        break
    elif lin[2] not in diffdiff and lin[1] not in diffdiff:
        pasli[int(lin[1])] = 1
        pasli[int(lin[2])] = 2
        diffdiff.update(lin[1:])
        poss *= 2
    elif lin[2] in diffdiff and lin[1] not in diffdiff:
        pasli[int(lin[1])] = abs(1 - pasli[int(lin[2])])
    elif lin[2] not in diffdiff and lin[1] in diffdiff:
        pasli[int(lin[2])] = abs(1 - pasli[int(lin[1])])
print poss
print pasli

fout = open("revegetate.out", "w")
x = str(bin(poss * (2 ** pasli.count(0))))
fout.write(x[2:])
fout.write("\n")"""
