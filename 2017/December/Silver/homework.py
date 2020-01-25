fin = open("homework.in", "r")
scorecount = int(fin.readline())
scorelist = map(int, fin.readline().split())
scorelist.insert(0, 0)

sumli = [0 for i in range(scorecount + 2)]
minli = [scorelist[-1] for i in range(scorecount + 2)]

for i in range(scorecount, -1, -1):
    sumli[i] = scorelist[i] + sumli[i + 1]
    minli[i] = min(minli[i + 1], scorelist[i])

#minli[0] = 0
print(scorelist)
print(sumli)
print(minli)

currsc = []
best = 0

for i in range(scorecount - 2, -1, -1):
    x = (sumli[i] - minli[i])/float(scorecount - i)
    if x > best:
        currsc = [i - 1]
        best = x
    elif x == best:
        currsc.insert(0, i + 1)

print(best, currsc)

fout = open("homework.out", "w")
for item in sorted(list(set(currsc))):
    fout.write(str(item) + "\n")
