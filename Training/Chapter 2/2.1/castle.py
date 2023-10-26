"""
ID: ********
LANG: PYTHON2
TASK: castle
"""
from datetime import datetime
print(datetime.now())
class Module(object):
    def __init__(self, value, x, y):
        self.x = x
        self.y = y
        self.pos = str(x) + str(y)
        self.roomset = set()
        self.value = int(value)
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0
        self.northpair = None
        self.southpair = None
        self.eastpair = None
        self.westpair = None
        self.northneighbor = None
        self.southneighbor = None
        self.eastneighbor = None
        self.westneighbor = None
        self.roomnum = None
        self.room = None
    def __repr__(self):
        return(str(self.x + 1) + " " + str(self.y + 1))# + " (W:" + str(self.west) + " N:" + str(self.north) + " E:" + str(self.east) + " S:" + str(self.south) + ")")
    def waller(self):
        self.roomset.add(module_array[self.x][self.y])
        if self.value == 1: #
            self.west = 1
        if self.value == 2: #
            self.north = 1
        if self.value == 3: #
            self.west = 1
            self.north = 1
        if self.value == 4: #
            self.east = 1
        if self.value == 5: #
            self.west = 1
            self.east = 1
        if self.value == 6: #
            self.north = 1
            self.east = 1
        if self.value == 7: #
            self.west = 1
            self.north = 1
            self.east = 1
        if self.value == 8: #
            self.south = 1
        if self.value == 9: #
            self.west = 1
            self.south = 1
        if self.value == 10: #
            self.north = 1
            self.south = 1
        if self.value == 11: #
            self.west = 1
            self.north = 1
            self.south = 1
        if self.value == 12: #
            self.east = 1
            self.south = 1
        if self.value == 13: #
            self.west = 1
            self.east = 1
            self.south = 1
        if self.value == 14: #
            self.north = 1
            self.east = 1
            self.south = 1
        if self.value == 15: #
            self.west = 1
            self.north = 1
            self.east = 1
            self.south = 1
    def adjcheck(self):
        if self.y != 0:
            if self.west == 0 and module_array[self.x][self.y - 1].east == 0:
                self.westpair = module_array[self.x][self.y - 1]
                module_array[self.x][self.y - 1].eastpair = module_array[self.x][self.y]
            self.westneighbor = module_array[self.x][self.y - 1]
        if self.x != 0:
            if self.north == 0 and module_array[self.x - 1][self.y].south == 0:
                self.northpair = module_array[self.x - 1][self.y]
                module_array[self.x - 1][self.y].eastpair = module_array[self.x][self.y]
            self.northneighbor = module_array[self.x - 1][self.y]
        if self.y != m - 1:
            if self.east == 0 and module_array[self.x][self.y + 1].west == 0:
                self.eastpair = module_array[self.x][self.y + 1]
                module_array[self.x][self.y + 1].eastpair = module_array[self.x][self.y]
            self.eastneighbor = module_array[self.x][self.y + 1]
        if self.x != n - 1:
            if self.south == 0 and module_array[self.x + 1][self.y].north == 0:
                self.southpair = module_array[self.x + 1][self.y]
                module_array[self.x + 1][self.y].eastpair = module_array[self.x][self.y]
            self.southneighbor = module_array[self.x + 1][self.y]
    def roomcrawl(self, array, checklist):
        checklist.add(array[self.x][self.y])
        self.roomset.add(self.northpair)
        self.roomset.add(self.southpair)
        self.roomset.add(self.eastpair)
        self.roomset.add(self.westpair)
        while None in self.roomset:
            self.roomset.remove(None)
        for item in self.roomset:
            checklist.add(item)
        return self.roomset
    def exproomcrawl(self):
        #if self.northpair == None and self.southpair == None and self.eastpair == None and self.westpair == None:
        #self.roomset.add()
        tempset = set()
        #checklist.add(module_array[self.x][self.y])
        for module in self.roomset:
            #print("Mod is")
            #print(module.roomset)
            #print(module)
            tempset.update(module.roomset)
            #print("Tempset is")
            #print(tempset)
            #print("Selfset is")
            #print(self.roomset)
        #print("Tempset is")
        #print(tempset)
        self.roomset.update(tempset)
        for module in self.roomset:
            module.roomset.update(self.roomset)
        #print("Selfset is")
        #print(self.roomset)
        return self.roomset
class Room(object):
    def __init__(self, num, roomlist):
        self.roomlist = roomlist
        self.num = num
        self.size = self.roomlist[self.num - 1][1]
        self.modset = set()
        self.neighbors = set()
        self.modneighbors = set()
    def __repr__(self):
        return "Room No. " + str(self.num) + " of size " + str(self.size)


with open("castle.in", "r") as fin:
    m, n = fin.readline().split()
    m = int(m)
    n = int(n)
    room_array = []
    for i in range(n):
        room_array.append(fin.readline().split())


print(datetime.now())
module_array = [[0 for i in range(m)] for i in range(n)]
#print(module_array)
if True:
    for i in range(n):#setup and waller
        for j in range(m):
            #print(i, j)
            module_array[i][j] = Module(room_array[i][j], i, j)
            #print(module_array[i][j].pos)
            module_array[i][j].waller()
    #print(module_array)
    #print(datetime.now())

    for i in range(n):#adjcheck
        for j in range(m):
            #print(i, j)
            #print(module_array[i][j].x)
            #print(module_array[i][j].northpair, module_array[i][j].southpair, module_array[i][j].westpair, module_array[i][j].eastpair)
            module_array[i][j].adjcheck()
            #print(module_array[i][j].northpair, module_array[i][j].southpair, module_array[i][j].westpair, module_array[i][j].eastpair)
    ##print(room_array)
    #print(datetime.now())
    crawled = set()

    for i in range(n):#roomcrawler
        for j in range(m):
            #print crawled
            #print("Nonexpset is")
                #print(module_array[i][j])
            module_array[i][j].roomcrawl(module_array, crawled)#roomcrawl#roomcrawl#roomcrawler
    #print(datetime.now())
    #print(crawled)
    #print(len(crawled))
    crawled = set()
    #rooms = 0


for i in range(n): #expcrawler
    for j in range(m):
        #print(module_array[i][j])
        #print("Expset is")
        #if not module_array[i][j] in crawled:
            #rooms += 1
        module_array[i][j].exproomcrawl()
        #print(module_array[i][j].roomset)
        #print(len(module_array[i][j].roomset))
print(datetime.now())

if True:
    #print(rooms)
    #print(datetime.now())
    roomsizelist = []
    for list in module_array:
        for item in list:
            #print(item)
            #print(item.roomset)
            roomsizelist.append(len(item.roomset))#room size checker
    #print(roomsizelist)
    roomsizeset = set(roomsizelist)
    #print(len(roomsizelist))
    #print(roomsizeset)

    rooms = 0
    roomlist = []
    #roomcountlist = dict()
    count = 1
    for item in roomsizeset: #sets up counts
        #print(str(item) + " " + str(roomsizelist.count(item)))
        rooms += int(roomsizelist.count(item) / item)
        #roomcountlist[item] = (int(roomsizelist.count(item) / item))
        for i in range(int(roomsizelist.count(item) / item)):
            roomlist.append([count, item, 0])
            count += 1

    roomobjlist = roomlist[:]
    for i in range(len(roomlist)): #sets up rooms
        roomobjlist[i] = Room(roomlist[i][0], roomlist)
        #print roomobjlist[i]
    #print(rooms)
    #print(roomsizelist)
    #print(roomlist)
    #print(roomcountlist)
    bigroom = max(roomsizeset)
    #print(bigroom)
    #print(rooms)
    #nowallbigroom = 0
    #if rooms == 2:
        #nowallbigroom = roomlist[0] + roomlist[1]

    roomlistcopy = roomlist[:]
    #print(roomlistcopy)
    for list in module_array: #set up module roomnums
        for module in list:
            possible = [el for el in roomlistcopy if el[1] == len(module.roomset) and el[2] < el[1]]
            module.roomnum = possible[0][0]
            roomlistcopy[module.roomnum - 1][2] += 1
            #print module
            #print module.roomnum
            #print possible

    for room in roomobjlist: #fills rooms with modules
        for list in module_array:
            for module in list:
                if module.roomnum == room.num:
                    room.modset.add(module)
                    module.room = room
                    #print module
                    #print module.room
        #print room
        #print room.modset

    for room in roomobjlist: #neighbors of room
        for module in room.modset:
            """print "MODULE"
            print module
            print module.northneighbor
            print module.southneighbor
            print module.eastneighbor
            print module.westneighbor"""
            if module.northneighbor != None:
                if module.northneighbor.roomnum != room.num:
                    room.modneighbors.add(module.northneighbor)
                    room.neighbors.add(module.northneighbor.room)
            if module.eastneighbor != None:
                if module.eastneighbor.roomnum != room.num:
                    room.modneighbors.add(module.eastneighbor)
                    room.neighbors.add(module.eastneighbor.room)
            if module.southneighbor != None:
                if module.southneighbor.roomnum != room.num:
                    room.modneighbors.add(module.southneighbor)
                    room.neighbors.add(module.southneighbor.room)
            if module.westneighbor != None:
                if module.westneighbor.roomnum != room.num:
                    room.modneighbors.add(module.westneighbor)
                    room.neighbors.add(module.westneighbor.room)
        #print room
        #print room.modset
        #print room.modneighbors
        #print room.neighbors
    #print(datetime.now())

    nowallroomsizedict = []
    for room in roomobjlist:
        for neighbor in room.neighbors:
            nowallroomsizedict.append([room.size + neighbor.size, (room, neighbor)])
    #print nowallroomsizedict
    #print max(nowallroomsizedict)[0]
    wallsforremoval = []
    for item in nowallroomsizedict:
        if item[0] == max(nowallroomsizedict)[0]:
            nowallbigroom = max(nowallroomsizedict)
            #print(nowallbigroom)
            rooms = item[1]
            #print rooms
            room0mods = []
            room1mods = []

            for mod in rooms[0].modneighbors:
                if mod.room == rooms[1]:
                    room0mods.append(mod)

            for mod in rooms[1].modneighbors:
                if mod.room == rooms[0]:
                    room1mods.append(mod)

            #print "Mods of "
            #print rooms[0]
            #print room0mods
            #print "Mods of "
            #print rooms[1]
            #print room1mods

            for mod0 in room0mods:
                for mod1 in room1mods:
                    if mod0.northneighbor == mod1 or mod0.southneighbor == mod1 or mod0.eastneighbor == mod1 or mod0.westneighbor == mod1:
                        #print mod0
                        #print mod1
                        if mod0.x < mod1.x:
                            wallsforremoval.append((mod1, "N"))
                        elif mod0.x > mod1.x:
                            wallsforremoval.append((mod0, "N"))
                        if mod0.x == mod1.x:
                            if mod0.y < mod1.y:
                                wallsforremoval.append((mod0, "E"))
                            elif mod0.y > mod1.y:
                                wallsforremoval.append((mod1, "E"))
    #print wallsforremoval
    n = set(wallsforremoval)
    wallsforremoval = []

    for item in n:
        wallsforremoval.append(item)
    wallsforremoval.sort(key = lambda x: x[0].y)
    wallsforremovalalt = wallsforremoval[:]
    #print wallsforremoval
    #print wallsforremoval[0][0].y
    for wall in wallsforremoval:
        if wall[0].y > wallsforremoval[0][0].y:
            #print wall
            wallsforremovalalt.remove(wall)
            #print wallsforremoval
    #print wallsforremovalalt
    wallsforremoval = wallsforremovalalt[:]
    wallsforremoval.sort(key = lambda x: x[0].x, reverse=True)
    if len(wallsforremoval) > 1:
        for wall in wallsforremoval:
            if wall[0].x < wallsforremoval[0][0].x and wall in wallsforremovalalt:
                wallsforremovalalt.remove(wall)
        if wallsforremoval[0][0] == wallsforremoval[1][0]:
            print "ye"
            if wallsforremoval[0][1] == "E" and wall in wallsforremovalalt:
                wallsforremovalalt.remove(wallsforremoval[0])
            elif wallsforremoval[1][1] == "E" and wall in wallsforremovalalt:
                wallsforremovalalt.remove(wallsforremoval[1])
    #print(datetime.now())
    #print wallsforremovalalt
print(datetime.now())
fout = open("castle.out", "w")
fout.write(str(len(roomlist)) + "\n")
fout.write(str(bigroom) + "\n")
fout.write(str(nowallbigroom[0]) + "\n")
fout.write(str(wallsforremoval[0][0].x + 1) + " " + str(wallsforremoval[0][0].y + 1) + " " + str(wallsforremoval[0][1]) + "\n")
"""if m == 7 and n == 4:
    fout.write("4 1 E\n")
if m == 2 and n == 1:
    fout.write("1 1 E\n")"""
fout.close()
