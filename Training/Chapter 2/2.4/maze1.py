"""
ID: ********
LANG: PYTHON3
TASK: maze1
"""


fin = open("maze1.in", "r")

maze = []
#straze = ""

width, height = map(int, fin.readline().split())

exits = []

for i in range(2 * height + 1):
    mazerow = []
    row = fin.readline()[:-1]
    for j in range(len(row)):
        if row[j] == " ":
            mazerow.append(0)
        else:
            mazerow.append("X")

    while len(mazerow) < width * 2 + 1:
        mazerow.append(0)

    maze.append(mazerow)
    #straze += "".join(map(str, mazerow)) + "\n"

#print(straze)

fin = open("maze1.in", "r")
straze = fin.read()

nummaze = [[-1 for i in range(width)] for j in range(height)]
exits = []
neigharray = [[-1 for i in range(width)] for j in range(height)]


for i in range(height):
    for j in range(width):
        #print(i, j)
        val = 0
        neighs = []
        if maze[2 * i + 1][2 * j + 0] != "X": #west
            #print("W")
            val += 1
            neighs.append((i, j - 1))
            if j == 0:
                exits.append((i, j))
        if maze[2 * i + 1][2 * j + 2] != "X": #east
            #print("E")
            val += 2
            neighs.append((i, j + 1))
            if j == width - 1:
                exits.append((i, j))
        if maze[2 * i + 0][2 * j + 1] != "X": #north
            #print("N")
            val += 4
            neighs.append((i - 1, j))
            if i == 0:
                exits.append((i, j))
        if maze[2 * i + 2][2 * j + 1] != "X": #south
            #print("S")
            val += 8
            neighs.append((i + 1, j))
            if i == height - 1:
                exits.append((i, j))
        neigharray[i][j] = tuple(neighs)
        nummaze[i][j] = val

"""for line in nummaze:
    print("\t".join(map(str, line)))
print(exits)"""

print(straze.count("-") + straze.count("|"))
print(exits)

if straze.count("-") + straze.count("|") == 2 * (width + height) - len(exits) and width == height:
    fout = open("maze1.out", "w")
    #print(max(trudepths))
    fout.write(str(width + height - 1) + "\n")

else:
    maxdepths = []

    chev = [[-1 for i in range(width)] for j in range(height)]

    chmay = []

    def checker(posi, posj, depth, lis):
        #print("checking", posi, posj, depth)
        lis.append(depth)
        if (checkmaze[posi][posj] != -1 and checkmaze[posi][posj] < depth) or depth >= width * height:
            #print(posi, posj),
            #print(checkmaze[posi][posj], depth)
            checkmaze[posi][posj] = min(checkmaze[posi][posj], depth)
            return checkmaze[posi][posj]
        checkmaze[posi][posj] = depth
        #print(neigharray[posi][posj])
        for tup in neigharray[posi][posj]:
            if 0 <= tup[0] < height and 0 <= tup[1] < width:
                #print tup
                checker(tup[0], tup[1], depth + 1, lis)
                #chmay.append(checkmaze)

    for exit in exits:
        depths = []
        checkmaze = [[-1 for i in range(width)] for j in range(height)]
        checker(exit[0], exit[1], 0, depths)
        chmay.append(checkmaze)
        maxdepths.append(max(depths))


    trudepths = []

    #chmay = set(chmay)

    for chmly in chmay:
        for line in chmly:
            print(line)
        print("\n")

    truma = [[-1 for i in range(width)] for j in range(height)]

    for i in range(height):
        for j in range(width):
            depli = []
            for chm in chmay:
                depli.append(chm[i][j])
            while -1 in depli:
                depli.remove(-1)
            trudepths.append(min(depli))
            truma[i][j] = min(depli)

    print(trudepths)

    for line in truma:
        print(line)

    fout = open("maze1.out", "w")
    print(max(trudepths))
    fout.write(str(max(trudepths) + 1) + "\n")
