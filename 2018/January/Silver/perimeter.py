fin = open("perimeter.in", "r")

n = int(fin.readline())
blobarray = []
bloblist = []
arli = [0]
perli = [0]
for i in range(n):
    blobarray.append(list(fin.readline()[:-1]))
    for j in range(n):
        if blobarray[i][j] == "#":
            bloblist.append((i, j))

#print(blobarray[0][1] == "#")
def FloodFill(node, color):
    if blobarray[node[0]][node[1]] == color:
        return None
    elif blobarray[node[0]][node[1]] == "#":
        
        blobarray[node[0]][node[1]] = color
        arli[color] += 1
        bloblist.remove(node)
        #c = 0
        #mess = []
        if node[0] == 0 or node[0] == n - 1:
            perli[color] += 1
            #c += 1
            #mess.append("N/S border")
        if node[0] > 0 and blobarray[node[0] - 1][node[1]] == ".":
            perli[color] += 1
            #c += 1
            #mess.append("N .")
        if node[0] < n - 1 and blobarray[node[0] + 1][node[1]] == ".":
            perli[color] += 1
            #c += 1
            #mess.append("S .")
        if node[1] == 0 or node[1] == n - 1:
            perli[color] += 1
            #c += 1
            #mess.append("E/W border")
        if node[1] > 0 and blobarray[node[0]][node[1] - 1] == ".":
            perli[color] += 1
            #c += 1
            #mess.append("W .")
        if node[1] < n - 1 and blobarray[node[0]][node[1] + 1] == ".":
            perli[color] += 1
            #c += 1
            #mess.append("E .")
        #print(node)
        #print(c)
        #print(mess)

        
        if 0 < node[0]:
            FloodFill((node[0] - 1, node[1]), color)
        if n - 1 > node[0]:
            FloodFill((node[0] + 1, node[1]), color)
        if 0 < node[1]:
            FloodFill((node[0], node[1] - 1), color)
        if n - 1 > node[1]:
            FloodFill((node[0], node[1] + 1), color)
        return None

currcol = 1
while len(bloblist) > 0:
    arli.append(0)
    perli.append(0)
    #for line in blobarray:
        #print(line)
    #print(bloblist)
    FloodFill(bloblist[0], currcol)
    currcol += 1
for line in blobarray:
        print(" ".join(map(str, line)))
print(arli)
print(perli)

maxar = max(arli)
minper = perli[arli.index(maxar)]
for i in range(currcol):
    if arli[i] == maxar and perli[i] < minper:
        minper = perli[i]

fout = open("perimeter.out", "w")
fout.write(str(maxar) + " " + str(minper) + "\n")
fout.close()
