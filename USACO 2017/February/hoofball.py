fin = open("hoofball.in", "r")

cowlist = []
passtolist = [0 for i in range(1001)]

cows = int(fin.readline())

def passto(cow):
    global cows
    ln = -1
    ld = 1000
    rn = -1
    rd = 1000
    #print(cow)
    for i in cowlist:
        if 0 < cow - i < ld:
            ln = i
            ld = cow - i

        if 0 < i - cow < rd:
            rn = i
            rd = i - cow
    #print(ln, ld)
    #print(rn, rd)
    if ld <= rd:
        #print(ln, ld)
        return ln
    else:
        #print(rn, rd)
        return rn

n = map(int, fin.readline().split())
for i in range(cows):
    cowlist.append(n[i])
for cow in cowlist:
    passtolist[passto(cow)] += 1
balls = 0
for cow in cowlist:
    #print(cow, passto(cow), passtolist[cow])
    pass
for cow in cowlist:
    if passtolist[cow] == 0:
        #print(cow)
        balls += 1
    if cow < passto(cow) and passto(passto(cow)) == cow and passtolist[cow] == 1 and passtolist[passto(cow)] == 1:
        #print(cow)
        balls += 1
#print(balls)
fout = open("hoofball.out", "w")
fout.write(str(balls) + "\n")
fout.close()
