fin = open("measurement.in", "r")

cowcarray = [["Mildred", "Bessie", "Elsie"]]
for i in range(100):
    cowcarray.append(["+0", "+0", "+0"])

maxday = 0
n = int(fin.readline())
for i in range(n):
    cowin = fin.readline().split()
    maxday = max(maxday, int(cowin[0]))
    cowcarray[int(cowin[0])][cowcarray[0].index(cowin[1])] = cowin[2]
cowmarray = [[7, 7, 7]]
for i in range(1, maxday + 1):
    cowmarray.append([eval(str(cowmarray[i - 1][0]) + cowcarray[i][0]), eval(str(cowmarray[i - 1][1]) + cowcarray[i][1]), eval(str(cowmarray[i - 1][2]) + cowcarray[i][2])])
cowdarray = [set() for i in range(maxday + 1)]

for i in range(1, maxday + 1):
    maxm = max(cowmarray[i])
    for j in range(3):
        if cowmarray[i][j] == maxm:
            cowdarray[i].update([cowcarray[0][j]])
cowdarray[0] = set(["Bessie", "Mildred", "Elsie"])
#for line in cowdarray:
    #print(line)
changecount = 0
for i in range(1, maxday + 1):
    if cowdarray[i] != cowdarray[i - 1]:
        changecount += 1

fout = open("measurement.out", "w")
fout.write(str(changecount) + "\n")
fout.close()
