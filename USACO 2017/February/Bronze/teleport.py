fin = open("teleport.in", "r")
coli = map(int, fin.readline().split())
ma = coli[0]
mb = coli[1]
ta = coli[2]
tb = coli[3]

mtm = abs(ma - mb)
mtt1 = abs(ma - ta) + abs(mb - tb)
mtt2 = abs(ma - tb) + abs(mb - ta)

fout = open("teleport.out", "w")
fout.write(str(min(mtm, mtt1, mtt2)) + "\n")
fout.close()
