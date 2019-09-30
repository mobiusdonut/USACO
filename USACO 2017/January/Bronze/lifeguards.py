fin = open("lifeguards.in", "r")

timearray = [0 for i in range(1000)]
shiftarray = []
mintime = 1000
maxtime = 0

n = int(fin.readline())
for i in range(n):
    shift = map(int, fin.readline().split())
    mintime = min(mintime, shift[0])
    maxtime = max(maxtime, shift[1])
    shiftarray.append([shift[0], shift[1]])
    for j in range(shift[0], shift[1]):
        timearray[j] += 1
#print(timearray[mintime:maxtime])
#print(mintime, maxtime)
maxtimesh = 0
for item in shiftarray:
    covered = 0
    for j in range(item[0], item[1]):
        timearray[j] -= 1
    #print(timearray[mintime:maxtime])
    for k in range(mintime, maxtime):
        if timearray[k] > 0:
            covered += 1
    for j in range(item[0], item[1]):
        timearray[j] += 1
    #print(covered)
    maxtimesh = max(maxtimesh, covered)

fout = open("lifeguards.out", "w")
fout.write(str(maxtimesh) + "\n")
fout.close()
