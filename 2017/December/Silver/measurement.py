fin = open("measurement.in", "r")

maxday = 0
n, milk = map(int, fin.readline().split())
cowlist = set([0])
daylist = set([0])
cowmarray = []
cowinlist = []

print("ye")
for i in range(n):
    #print(cowmarray)
    cowin = fin.readline().split()
    cowinlist.append(cowin)
    daylist.add(cowin[0])
    cowlist.add(cowin[1])
daylist = list(daylist)
cowlist = list(cowlist)
for i in range(1):
    cowinlist.sort(key = lambda x: int(x[0]))
    #print(cowinlist)
    cowmarray.append(cowlist)
    x = [milk for i in range(len(cowlist))]
    x[0] = 0
    cowmarray.append(x)
print("ye")
for i in range(len(cowinlist)):
    #for line in cowmarray:
        #print(line)
    #print("\n")

    cowmarray[i + 1][0] = cowinlist[i][0]
    #print(cowmarray[0])
    cowmarray[i + 1][cowmarray[0].index(cowinlist[i][1])] = eval(str(cowmarray[i + 1][cowmarray[0].index(cowinlist[i][1])]) + cowinlist[i][2])
    if i != len(cowinlist) - 1:
        cowmarray.append(cowmarray[-1][:])
for line in cowmarray:
    print(line)
print("ye")
cowdarray = [set() for i in range(1, len(daylist) + 1)]
cowdarray[0].update(set(cowlist[1:]))
#print(cowdarray)
for i in range(1, len(daylist)):
    for j in range(1, len(cowlist)):
        #print(i, j)
        if cowmarray[i][j] == max(cowmarray[i][1:]):
            cowdarray[i].add(cowmarray[0][j])

x = 0
for i in range(1, len(cowdarray)):
    if cowdarray[i] != cowdarray[i - 1]:
        x += 1
        #print(cowdarray[i], cowdarray[i - 1])

"""for i in range(1, len(daylist)):
    if cowdarray[i] != cowdarray[i - 1]:
        print(cowdarray[i])
        print(cowmarray[0])
        print(cowmarray[i])"""
fout = open("measurement.out", "w")
fout.write(str(x) + "\n")
fout.close()
