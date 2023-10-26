"""
ID: ********
LANG: PYTHON3
TASK: money
"""

fin = open("money.in", "r")
v, n = map(int, fin.readline().split())
coins = []
for i in range(v):
    coins.extend(fin.readline().split())
#coinc <= 25 (v)
#tar <= 10000 (n)

for item in coins[:]:
    coins[coins.index(item)] = int(item)

print(v)
print(n)
print(coins)

curray = [[0] * (v + 2) for i in range(n + 2)]

for i in range(v + 1):
    curray[0][i] = 1
for i in range(n + 1):
    curray[i][0] = 0
for i in range(1, v + 1):
    for j in range(1, n + 1):
        #for d in curray:
            #print d
        #print ""
        if j - coins[i - 1] >= 0:
            curray[j][i] = curray[j][i - 1] + curray[j - coins[i - 1]][i]
        else:
            curray[j][i] = curray[j][i - 1]

#print len(curray)
#print len(curray[0])

print(curray[n][v])

fout = open("money.out", "w")
fout.write(str(curray[n][v]) + "\n")
fout.close()
