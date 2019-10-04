"""
ID: kripaki1
LANG: PYTHON3
TASK: lamps
"""

with open("lamps.in", "r") as fin:
    lamps = int(fin.readline())
    clicks = int(fin.readline())
    onlamps = map(int, fin.readline().split())
    offlamps = map(int, fin.readline().split())
    onlamps = list(onlamps)
    offlamps = list(offlamps)
    onlamps.remove(-1)
    offlamps.remove(-1)
#print(lamps)
#print(clicks)
#print(onlamps)
#print(offlamps)

possibilities = []

def button1(lamplist):
    llist = lamplist[:]
    for i in range(0, lamps, 1):
        if llist[i] == 0:
            llist[i] = 1
        elif llist[i] == 1:
            llist[i] = 0
    #print llist
    return llist
def button2(lamplist):
    llist = lamplist[:]
    for i in range(1, lamps, 2):
        if llist[i] == 0:
            llist[i] = 1
        elif llist[i] == 1:
            llist[i] = 0
    #print llist
    return llist
def button3(lamplist):
    llist = lamplist[:]
    for i in range(0, lamps, 2):
        if llist[i] == 0:
            llist[i] = 1
        elif llist[i] == 1:
            llist[i] = 0
    #print llist
    return llist
def button4(lamplist):
    llist = lamplist[:]
    for i in range(0, lamps, 3):
        if llist[i] == 0:
            llist[i] = 1
        elif llist[i] == 1:
            llist[i] = 0
    #print llist
    return llist

def legalCheck(lamplist, onlist, offlist):
    legal = True
    for lamp in onlist:
        if lamplist[lamp - 1] == 0:
            legal = False
    for lamp in offlist:
        if lamplist[lamp - 1] == 1:
            legal = False
    if legal == True:
        return True
    else:
        return False

lamplist = [1 for i in range(lamps)]
#print(button1(lamplist))
#print
move_array = [[[[None for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)]

move_array[0][0][0][0] = lamplist
#print move_array[0][0][0][0]
#print
move_array[1][0][0][0] = button1(lamplist)
move_array[0][1][0][0] = button2(lamplist)
move_array[0][0][1][0] = button3(lamplist)
move_array[0][0][0][1] = button4(lamplist)

move_array[1][1][0][0] = button1(button2(lamplist))
move_array[1][0][1][0] = button1(button3(lamplist))
move_array[1][0][0][1] = button1(button4(lamplist))
move_array[0][1][1][0] = button2(button3(lamplist))
move_array[0][1][0][1] = button2(button4(lamplist))
move_array[0][0][1][1] = button3(button4(lamplist))

move_array[1][1][1][0] = button1(button2(button3(lamplist)))
move_array[1][1][0][1] = button1(button2(button4(lamplist)))
move_array[1][0][1][1] = button1(button3(button4(lamplist)))
move_array[0][1][1][1] = button2(button3(button4(lamplist)))

move_array[1][1][1][1] = button1(button2(button3(button4(lamplist))))

#print move_array

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                if (legalCheck(move_array[i][j][k][l], onlamps, offlamps)) == True and (clicks - (i + j + k + l)) % 2 == 0 and i + j + k + l <= clicks:
                    #print(i, j, k, l)
                    #print (clicks - (i + j + k + l)) % 2
                    #print move_array[i][j][k][l]
                    possibilities.append("".join(map(str, move_array[i][j][k][l])))

print(possibilities)
possibilities.sort()

fout = open("lamps.out", "w")
if len(possibilities) > 0:
    for item in possibilities:
        fout.write(item + "\n")
else:
    fout.write("IMPOSSIBLE\n")
fout.close()
