fin = open("shuffle.in", "r")
cownt = int(fin.readline())
shuff = map(int, fin.readline().split())
cows = map(str, fin.readline().split())
print(cows)

def revshuff(shuffer, cowli):
    cowtem = cowli[:]
    #print(cowtem)
    for i in range(len(shuffer)):
        #print(i, cowtem[i])
        cowtem[i] = cowli[shuffer[i] - 1]
    return cowtem

endcows = (revshuff(shuff, revshuff(shuff, revshuff(shuff, cows))))

fout = open("shuffle.out", "w")
for cow in endcows:
    fout.write(cow + "\n")
fout.close()
