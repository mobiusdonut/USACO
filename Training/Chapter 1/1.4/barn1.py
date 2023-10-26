"""
ID: ********
LANG: PYTHON2
TASK: barn1
"""

with open("barn1.in", "r") as fin:
    maxboards, stalls, cows = map(int, fin.readline().split())
    cow_list = list(map(int, fin.read()[:-1].split("\n")))
    cow_list.sort()
    #print maxboards
    #print stalls
    #print cows
    #print cow_list

minstalls = 0
if maxboards >= cows:
    minstalls = cows
else:
    gaps = [(cow_list[i+1] - cow_list[i] - 1) for i in range(cows-1)]
    gaps.sort()
    #print gaps
    maxgaps = 0
    for i in range(maxboards - 1): #maxboards means maxboards - 1 gaps in between
        maxgaps += gaps.pop()
        #print maxgaps
    minstalls = max(cow_list) - min(cow_list) + 1 - maxgaps

fout = open("barn1.out", "w")
fout.write(str(minstalls) + "\n")
fout.close()
