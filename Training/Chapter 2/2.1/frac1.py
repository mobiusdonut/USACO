"""
ID: kripaki1
LANG: PYTHON3
TASK: frac1
"""

def gcd(a, b):
    afac = set()
    bfac = set()
    for i in range(1, a + 1):
        if a % i == 0:
            afac.add(i)
    #print afac
    for j in range(1, b + 1):
        if b % j == 0:
            bfac.add(j)
    #print bfac
    return max(afac.intersection(bfac))

#print gcd(12, 8)

with open("frac1.in", "r") as fin:
    N = int(fin.readline())
#print N
fracdict = dict()
for i in range(2, N + 1):
    for j in range(1, i):
        if gcd(i, j) == 1:
            fracdict[float(j)/float(i)] = str(j) + "/" + str(i) + "\n"
fraclist = sorted(fracdict)
print(fracdict)
print(fraclist)
fout = open("frac1.out", "w")
fout.write("0/1\n")
for frac in fraclist:
    fout.write((fracdict[frac]))
fout.write("1/1\n")
fout.close()
