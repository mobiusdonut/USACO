"""
ID: ********
LANG: PYTHON3
TASK: numtri
"""

numtree = []

with open("numtri.in", "r") as fin:
    rows = int(fin.readline())
    for i in range(rows):
        line = fin.readline()
        numtree.append(line.split())
#print(numtree)

sums = [[0 for i in range(rows)] for j in range(2)]
#print(sums)


for z in range(rows):
    sums[(rows - 1) % 2][z] = int(numtree[rows - 1][z])
#print(sums)
#initializes with bottom row(top if odd, bottom if even)

for y in range(rows - 2, -1, -1):
    for x in range(y + 1):
        #print(max(sums[(y + 1) % 2][x], sums[(y + 1) % 2][x + 1]))
        #print(numtree[y][x])
        sums[y % 2][x] = max(sums[(y + 1) % 2][x], sums[(y + 1) % 2][x + 1]) + int(numtree[y][x])
        #print(sums)
        #each row above stores adds maximum of those below it to itself
#print(sums)
maxsum = sums[0][0]
"""def brancher(posx, posy):
    total = numtree[posx][posy]
    #print(total)
    if posx == len(numtree) - 1:
        #print("End of tree!")
        return total
    else:
        #print("The max is " + str(max(brancher(posx + 1, posy), brancher(posx + 1, posy + 1))))
        #print(total)
        total = int(total) + int(max(brancher(posx + 1, posy), brancher(posx + 1, posy + 1)))
        #print(total)
        return total
maxsum = str(brancher(0, 0))"""

fout = open("numtri.out", "w")
fout.write(str(maxsum) + "\n")
fout.close()
