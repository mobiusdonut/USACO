fin = open("shuffle.in", "r")
n = int(fin.readline())
moveto = [-1 for i in range(n)]
movelist = map(int, fin.readline().split())
status = [0 for i in range(n)]

for i in range(n):
    #print(i)
    moveto[i] = movelist[i] - 1
    #print(str(i) + " " + str(movelist[i] - 1))
def looper(i):
    used = []
    while status[i] == 0:
        used.append(i)
        status[i] = 1
        i = moveto[i]
    if i in used:
        for item in used[used.index(i):]:
            status[item] = 2
        print(used[used.index(i):])
for i in range(n):
    if status[i] == 0:
        looper(i)
#print(status)

def cowloop():
    cows = [1 for i in range(n)]
    for i in range(n/2):
        print(cows)
        for i in range(n):
            x = cows[i]
            cows[moveto[i]] += x
            cows[i] -= x

fout = open("shuffle.out", "w")
fout.write(str(status.count(2)) + "\n")
fout.close()
