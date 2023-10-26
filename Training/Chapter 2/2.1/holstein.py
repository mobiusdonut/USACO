"""
ID: ********
LANG: PYTHON2
TASK: holstein
"""


with open("holstein.in", "r") as fin:
    vitamins = int(fin.readline())
    requirements = map(int, fin.readline().split())
    feeds = int(fin.readline())
    vitafeedarray = []
    for i in range(feeds):
        vitafeedarray.append(map(int, fin.readline().split()))

#print(vitafeedarray)
best = [None for i in range(feeds)]
bestCurrent = feeds
feedset = []

def better(count, used):
    if count < bestCurrent:
        return True
    if count > bestCurrent:
        return False
    for i in range(feeds):
        if used[i] and (not best[i]):
            return True
        if (not used[i]) and best[i]:
            return False
    return False
def recurfeed(feed, used, count, vit):
    global best
    if feed == len(used):
        for i in range(vitamins):
            if vit[i] < requirements[i]:
                return None
        if better(count, used) == True:
            bestCurrent = count
            best = used[:]
            feedset.append(best)
            return None
    recurfeed(feed + 1, used, count, vit)
    for i in range(vitamins):
        vit[i] += vitafeedarray[feed][i]
    used[feed] = True
    recurfeed(feed + 1, used, count + 1, vit)
    for i in range(vitamins):
        vit[i] -= vitafeedarray[feed][i]
    used[feed] = False

G = [False for i in range(feeds)]
V = [0 for i in range(vitamins)]

recurfeed(0, G, 0, V)
#print(feedset)
feedsetnum = []
for item in feedset:
    n = 0
    numly = []
    #print item
    for i in range(len(item)):
        if item[i] == True:
            n += i + 1
            numly.append(i + 1)
    numly.insert(0, n)
    #print numly
    feedsetnum.append(numly)
feedsetnum.sort(key=lambda x: len(x))
print(feedsetnum)
bestcombo = feedsetnum[0]
for item in feedsetnum:
    if len(item) < len(bestcombo):
        bestcombo = item
    if len(item) == len(bestcombo) and item[0] < bestcombo[0]:
        bestcombo = item
print bestcombo

fout = open("holstein.out", "w")
fout.write(str(len(bestcombo) - 1))
for item in bestcombo[1:]:
    fout.write(" " + str(item))
fout.write("\n")
fout.close()
