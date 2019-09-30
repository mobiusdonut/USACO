fin = open("taming.in", "r")
log = []
days = int(fin.readline())
taken = [0 for i in range(days)]
day = 0
inc = False
for item in map(int, fin.readline().split()):
    if inc:
        break
    log.append(item)
    day += 1
    if item != -1:
        #taken[day - item:day + 1] = [1] * (item + 1)
        x = 0
        for i in range(day - 1, day - item - 2, -1):
            taken[i] = 1
            if log[i] != -1 and log[i] != item - x:
                inc = True
                break
            else:
                log[i] = item - x
            x += 1

taken[0] = 1
log[0] = 0
print(log)
print(taken)
logli = "".join(map(str, taken))

fout = open("taming.out", "w")
if not inc:
    min = log.count(0)
    max = min + log.count(-1)
    fout.write(str(min) + " " + str(max) + "\n")
else:
    fout.write("-1\n")
fout.close()
