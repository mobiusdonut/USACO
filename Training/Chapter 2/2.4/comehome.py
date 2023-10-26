"""
ID: ********
LANG: PYTHON2
TASK: comehome
"""
fin = open("comehome.in", "r")
n = int(fin.readline())
pinfos = []
paslist = set()
for i in range(n):
    pinfo = fin.readline().split()
    pinfos.append(pinfo)
    paslist.update(pinfo[0])
    paslist.update(pinfo[1])
print(pinfos)
paslist = list(paslist)
paslist.sort()
print(paslist)
caps = paslist.index("Z")
psarray = [[0 for i in range(len(paslist) + 1)] for i in range(len(paslist) + 1)]
for i in range(1, len(paslist) + 1):
    psarray[0][i] = paslist[i - 1]
    psarray[i][0] = paslist[i - 1]
for item in pinfos:
    psarray[psarray[0].index(item[0])][psarray[0].index(item[1])] = int(item[2])
    psarray[psarray[0].index(item[1])][psarray[0].index(item[0])] = int(item[2])
if n <= 650:
    for i in range(n):
        for i in range(1, caps + 1):
            for j in range(i + 1, len(psarray)):
                if psarray[i][j] != 0:
                    for k in range(i + 1, len(psarray)):
                        #print(i, j, k)
                        if psarray[k][j] != 0:
                            if psarray[i][k] != 0:
                                psarray[i][k] = min(psarray[i][k], psarray[i][j] + psarray[k][j])
                                psarray[k][i] = min(psarray[i][k], psarray[i][j] + psarray[k][j])
                            else:
                                psarray[i][k] = psarray[i][j] + psarray[k][j]
                                psarray[k][i] = psarray[i][j] + psarray[k][j]
else:
    n = 1001
    for i in range(26, 52):
        print(i, n)
        n = min(n, psarray[26][i] + psarray[1 + i][i - 25])

#for line in psarray:
    #print(" ".join(map(str, line)))
z = psarray[0].index("Z")
zlist = psarray[caps + 1][1:caps + 1]
zset = set(zlist)
zset = list(zset)
if 0 in zset:
    zset.remove(0)
#print(zlist)
#print(zset)
fout = open("comehome.out", "w")
fout.write(paslist[zlist.index(min(zset))] + " " + str(min(zset)) + "\n")
print(paslist[zlist.index(min(zset))] + " " + str(min(zset)) + "\n")
fout.close()
