"""
ID: ********
LANG: PYTHON3
TASK: ariprog
"""

with open("ariprog.in", "r") as fin:
    n = int(fin.readline().rstrip()) #progression length
    m = int(fin.readline().rstrip()) #upper limit for bisquares
#print(proglength)
#print(squarebound)
#print(proglength + squarebound)
bisquares = [False for i in range(2 * m ** 2 + 1)]
#print(bisquares)
for p in range(m + 1):
    for q in range(p, m + 1):
        bisquare = p ** 2 + q ** 2
        #print bisquare
        bisquares[bisquare] = True
#bisquares = list(bisquares)
#bisquares.sort()
aribi = []
#n = max(bisquares)
#print(bisquares)
count12 = []
not12 = []
"""if m <= n:
    a = 0
    while a + (n - 1) <= 2 * m ** 2:
        if bisquares[a] == True:
            #print(a)
            for b in range(1, len(bisquares) // (n - 1) + 1):
                if a + (n - 1) * b > 2 * m ** 2:
                    break
                ok = True
                for seq in range(n):
                    num = a + seq * b
                    if bisquares[num] == False:
                        ok = False
                        break
                if ok:
                    print(a, b)
                    aribi.append((b, a))
        a = a + 1"""
if n >= 14:
    a = 0
    while a + (n - 1) <= 2 * m ** 2:
        if bisquares[a] == True:
            #print(a)
            for b in range(1, (len(bisquares) // (n - 1) + 1) // 84 + 1):
                if a + (n - 1) * b * 84 > 2 * m ** 2:
                    break
                ok = True
                for seq in range(n):
                    num = a + seq * b * 84
                    if bisquares[num] == False:
                        ok = False
                        break
                if ok:
                    #print(a, b * 4)
                    aribi.append((b * 84, a))
                    #if (b * 4) % 84 == 0 and not(b in count12):
                        #count12.append(b * 4)
                    #elif not(b * 4 in not12) and not(b in count12):
                        #not12.append(b * 4)
        a = a + 1
elif n >= 6:
    a = 0
    while a + (n - 1) <= 2 * m ** 2:
        if bisquares[a] == True:
            #print(a)
            for b in range(1, (len(bisquares) // (n - 1) + 1) // 12 + 1):
                if a + (n - 1) * b * 12 > 2 * m ** 2:
                    break
                ok = True
                for seq in range(n):
                    num = a + seq * b * 12
                    if bisquares[num] == False:
                        ok = False
                        break
                if ok:
                    #print(a, b * 4)
                    aribi.append((b * 12, a))
                    #if (b * 4) % 84 == 0 and not(b in count12):
                        #count12.append(b * 4)
                    #elif not(b * 4 in not12) and not(b in count12):
                        #not12.append(b * 4)
        a = a + 1
elif n >= 4:
    a = 0
    while a + (n - 1) <= 2 * m ** 2:
        if bisquares[a] == True:
            #print(a)
            for b in range(1, (len(bisquares) // (n - 1) + 1) // 4 + 1):
                if a + (n - 1) * b * 4 > 2 * m ** 2:
                    break
                ok = True
                for seq in range(n):
                    num = a + seq * b * 4
                    if bisquares[num] == False:
                        ok = False
                        break
                if ok:
                    #print(a, b * 4)
                    aribi.append((b * 4, a))
                    #if (b * 4) % 84 == 0 and not(b in count12):
                        #count12.append(b * 4)
                    #elif not(b * 4 in not12) and not(b in count12):
                        #not12.append(b * 4)
        a = a + 1
else:
    a = 0
    while a + (n - 1) <= 2 * m ** 2:
        if bisquares[a] == True:
            #print(a)
            for b in range(1, (len(bisquares) // (n - 1) + 1) + 1):
                if a + (n - 1) * b > 2 * m ** 2:
                    break
                ok = True
                for seq in range(n):
                    num = a + seq * b
                    if bisquares[num] == False:
                        ok = False
                        break
                if ok:
                    #print(a, b * 4)
                    aribi.append((b, a))
                    #if (b) % 4 == 0 and not(b in count12):
                        #count12.append(b)
                    #elif not(b in not12) and not(b in count12):
                        #not12.append(b)
        a = a + 1
#print(aribi)
aribi.sort()
#print aribi
#print(len(bisquares) // (n - 1))
#print(len(bisquares))
#print("a")
print(count12)
print(not12)
"""for a in bisquares:
    if a + (n - 1) > 2 * m ** 2:
        break
    for b in range(1, int((max(bisquares) - min(bisquares)/5))):
        if a + (n - 1) * b > 2 * m ** 2:
            break
        ok = True
        for seq in range(n):
            num = a + seq * b
            if not(num in bisquares):
                ok = False
                break
        if ok == True:
            aribi.append([b, a])
#print aribi
aribi.sort()
print(aribi)
"""
fout = open("ariprog.out", "w")
if len(aribi) == 0:
    fout.write("NONE\n")
else:
    for item in aribi:
        fout.write(str(item[1]) + " " + str(item[0]) + "\n")
fout.close()
