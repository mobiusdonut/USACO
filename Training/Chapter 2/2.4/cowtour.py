"""
ID: ********
LANG: PYTHON3
TASK: cowtour
"""

class Pasture(object):
    def __init__(self, num, posx, posy):
        self.num = num
        self.x = posx
        self.y = posy
        self.neighbors = {}
    def __repr__(self):
        return("Pasture " + str(self.num) + ": " + str(self.x) + " " + str(self.y))

fin = open("cowtour.in", "r")
pcount = int(fin.readline())

plist = []

for i in range(pcount):
    coords = map(int, fin.readline().split())
    plist.append(Pasture(i, coords[0], coords[1]))

"""for item in plist:
    print(item)"""

adjmatr = []

for i in range(pcount):
    adjmatr.append(list(fin.readline()[:-1]))

"""for line in adjmatr:
    print(line)"""


for i in range(pcount):
    for j in range(pcount):
        #print(j)
        if adjmatr[i][j] == "1":
            plist[i].neighbors[plist[j]] = round(((plist[j].x - plist[i].x) ** 2 + (plist[j].y - plist[i].y) ** 2) ** 0.5, 6)

"""for item in plist:
    print(item)
    print(item.neighbors)"""

distmatr = [[-1 for i in range(pcount)] for i in range(pcount)]
#print(distmatr)

for i in range(pcount):
    distmatr[i][i] = 0

j = 0
for p1 in plist:
    for p2 in plist:
        if p1 != p2:
            if p2 in p1.neighbors.keys():
                distmatr[p1.num][p2.num] = p1.neighbors[p2]
for line in distmatr:
    print(line)
