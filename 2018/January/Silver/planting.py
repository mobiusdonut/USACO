fin = open("planting.in", "r")

fields = int(fin.readline())
fieldcon = [[None for i in range(fields + 1)] for i in range(fields + 1)]
grasslist = [None for i in range(fields)]
for i in range(fields - 1):
    f = list(map(int, fin.readline().split()))
    fieldcon[f[0]][f[1]] = 0
    fieldcon[f[1]][f[0]] = 0
for line in fieldcon:
    print("\t".join(map(str, line)))

def Grasser(field):
    for i in range(1, 
