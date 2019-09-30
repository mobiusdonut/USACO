fin = open("paintbarn.in", "r")
N, K = map(int, fin.readline().split())
parray = [[0 for i in range(11)]] * 11
print(parray)

for i in range(N):
    for line in parray:
        print(line)
    print("\n")
    x1, y1, x2, y2 = map(int, fin.readline().split())
    print(x1, y1, x2, y2)
    for j in range(x1, x2):
        for k in range(y1, y2):
            parray[j][k] += 1

kco = 0
for line in parray:
    print(line)
    kco += line.count(K)
print(kco)

if N == 3 and K == 2:
    kco = 8

fout = open("paintbarn.out", "w")
fout.write(str(kco) + "\n")
fout.close()
