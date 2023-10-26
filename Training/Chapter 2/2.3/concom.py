"""
ID: ********
LANG: PYTHON3
TASK: concom
"""

fin = open("concom.in", "r")
compc = int(fin.readline())

controls = [[False] * (101) for i in range(101)]
owns = [[0] * (101) for i in range(101)]

#print compc

for i in range(1, 101):
    #print i
    owns[i][i] = 100
    controls[i][i] = True

def new_control(a, b):
    if controls[a][b]:
        return None
    controls[a][b] = True

    for i in range(101): #a owns what b owns
        owns[a][i] += owns[b][i]
        if owns[a][i] > 100:
            owns[a][i] = 100

    for i in range(101): #what owns a owns b
        if controls[i][a]:
            new_control(i, b)

    for i in range(101): #changes in a ownership in case of cycle
        if owns[a][i] > 50:
            new_control(a, i)

def more_control(a, b, perce):
    for i in range(1, 101):
        if controls[i][a]:
            owns[i][b] += perce
            if owns[i][b] > 100:
                owns[i][b] = 100
    for i in range(1, 101):
        if owns[i][b] > 50:
            new_control(i, b)

for i in range(compc):
    contrcomb = fin.readline().split()
    #print(contrcomb)
    a = int(contrcomb[0])
    b = int(contrcomb[1])
    p = int(contrcomb[2])
    #print(a, b, p)
    if p == 100:
        #print("Company owns 100%")
        controls[a][b] = True
        owns[a][b] = 100
    more_control(a, b, p)

"""for line in controls:
    print line
for line in owns:
    print line"""

#print(controls[30][80])
#print(owns[30][80])

fout = open("concom.out", "w")
for i in range(1, 101):
    #print("ye")
    for j in range(1, 101):
        if i != j and controls[i][j]:
            #print("ye")
            print(i, j)
            fout.write(str(i) + " " + str(j) + "\n")
fout.close()
