"""
ID: kripaki1
LANG: PYTHON2
TASK: castle
"""

with open("castle.in", "r") as fin:
    m, n = fin.readline().split()
    m = int(m)
    n = int(n)
    mod_array = []
    for i in range(n):
        mod_array.append(map(int, fin.readline().split()))

#print(mod_array)
room_array = [[-1 for i in range(m)] for i in range(n)] #x is up/down, y is left/right
#print(room_array)

def floodFillRooms(x, y, room):
    #print(x, y)
    def westNeigh(x, y):
        if '{0:04b}'.format(mod_array[x][y])[-1] == "0":
            return True
        return False
    def northNeigh(x, y):
        if '{0:04b}'.format(mod_array[x][y])[-2] == "0":
            return True
        return False
    def eastNeigh(x, y):
        if '{0:04b}'.format(mod_array[x][y])[-3] == "0":
            return True
        return False
    def southNeigh(x, y):
        if '{0:04b}'.format(mod_array[x][y])[-4] == "0":
            return True
        return False

    if room_array[x][y] != -1: #module already counted
        return 0
    room_array[x][y] = room
    roomsize = 1

    if westNeigh(x, y) == True:
        #print True
        roomsize += floodFillRooms(x, y - 1, room)
    if northNeigh(x, y) == True:
        #print True
        roomsize += floodFillRooms(x - 1, y, room)
    if eastNeigh(x, y) == True:
        #print True
        roomsize += floodFillRooms(x, y + 1, room)
    if southNeigh(x, y) == True:
        #print True
        roomsize += floodFillRooms(x + 1, y, room)
    return roomsize

biggestsize = 0
roomcount = 0
roomsizedict = dict()
for i in range(n):
    for j in range(m):
        if room_array[i][j] != -1:
            continue
        #print(i, j)
        size = floodFillRooms(i, j, roomcount)
        roomsizedict[roomcount] = size
        roomcount += 1
        if size > biggestsize:
            biggestsize = size
#print(biggestsize)

bestsize = 0
bestX = 0
bestY = 0
bestDirection = None

for j in range(m):
    for i in range(n - 1, -1, -1):
        if i + 1 < n and room_array[i][j] != room_array[i + 1][j]:
            s = roomsizedict[room_array[i][j]] + roomsizedict[room_array[i + 1][j]]
            if s > bestsize:
                bestsize = s
                bestX = i + 1
                bestY = j
                bestDirection = "N"
    for i in range(n - 1, -1, -1):
        if j + 1 < m and room_array[i][j] != room_array[i][j + 1]:
            e = roomsizedict[room_array[i][j]] + roomsizedict[room_array[i][j + 1]]
            if e > bestsize:
                bestsize = e
                bestX = i
                bestY = j
                bestDirection = "E"
fout = open("castle.out", "w")
fout.write(str(roomcount) + "\n")
fout.write(str(biggestsize) + "\n")
fout.write(str(bestsize) + "\n")
fout.write(str(bestX + 1) + " " + str(bestY + 1) + " " + bestDirection + "\n")
fout.close()
