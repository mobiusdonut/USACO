fin = open("convention.in", "r")
n, m, c = map(int, fin.readline().split())
tlist = map(int, fin.readline().split())
tlist.sort()
#print(tlist)
mins = []

if n == m * c:
    for i in range(n // c):
        mins.append(tlist[i * c + c - 1] - tlist[i * c])
else:
    for i in range(n // c):
        mins.append(tlist[i * c + c - 1] - tlist[i * c])
    for i in range(m - n // c):
        x = max(mins)
        del tlist[mins.index(x) * c]
    #print(mins)
    mins = []
    for i in range(n // c):
        mins.append(tlist[i * c + c - 1] - tlist[i * c])

#print(mins)

fout = open("convention.out", "w")
fout.write(str(max(mins)) + "\n")
fout.close()
