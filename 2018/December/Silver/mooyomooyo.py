fin = open("mooyomooyo.in", "r")
n, k = map(int, fin.readline().split())
blist = []
barray = []

for i in range(n):
    x = fin.readline()
    blist.append(x)
    barray.append(list(x)[:-1])
