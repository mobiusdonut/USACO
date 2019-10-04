"""
ID: kripaki1
LANG: PYTHON3
TASK: wormhole
"""

class Wormhole(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pair = None
    def __repr__(self): #for printing purposes
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def nextWormhole(self):
        for obj in wormholes:
            if obj.y == self.y and obj.x > self.x:
                return obj

with open("wormhole.in", "r") as fin:
    N = int(fin.readline())
    wormholes = []
    for i in range(N):
        x, y = map(int, fin.readline().split())
        wormholes.append(Wormhole(x, y))
wormholes.sort(key = lambda worm: worm.x)
#a = wormholes[0]
#print(wormholes)
#print(a.nextWormhole())

def pairWormholes(wormpair):
    worm1 = wormpair[0]
    worm2 = wormpair[1]
    worm1.paired = worm2
    worm2.paired = worm1

def pairGenerator(wormlist):
    #returns all possible combinations of pairs in given coordinations
    l = list(wormlist)

    if len(l) == 2:
        return [[(l[0], l[1])]]

    result = []
    i = 0
    for j in range(1,len(wormlist)): #recursion: applies pairgenerator on list of wormholes minus the two paired
        rests = pairGenerator([x for x in wormlist if (x != l[i] and x != l[j])])
        pairset = [[(l[i],l[j])] + rest for rest in rests]
        #print rests
        #print pairset
        result += pairset
    return result

pairlist = pairGenerator(wormholes)
#print pairlist
loopcount = 0
for pairings in pairlist:
    for p in pairings:
        pairWormholes(p)

    loop = False
    for c in set(wormholes):
        route = set()       # list of entrances of wormhole visited

        while True:
            n = c.paired    # exit of wormhole
            if n in route:
                loop = True
                #print route
                break
            route = route.union({n})
            if n.nextWormhole() is None:    # no further wormholes to encounter # if not
                break
            else:
                c = n.nextWormhole()

        if loop == True and len(route) > 1:    # if discovered a loop, no need to consider
            break
    if loop == True:
        loopcount += 1
#print loopcount
fout = open("wormhole.out", "w")
fout.write(str(loopcount) + "\n")
fout.close()
