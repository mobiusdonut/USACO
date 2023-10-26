"""
ID: ********
LANG: PYTHON3
TASK: milk3
"""
with open("milk3.in", "r") as fin:
    A, B, C = map(int, fin.readline().split())
capacity = [A, B, C]
start = [0, 0, C]
possible_setups = [[[0 for i in range(21)]for i in range(21)]for i in range(21)]

def pourMilk(milklist, fromb, tob):
    pour = milklist[fromb]
    if pour > capacity[tob] - milklist[tob]:
        pour = capacity[tob] - milklist[tob]
    milklist[fromb] -= pour
    milklist[tob] += pour
#print(possible_setups)

def milkSolve(milklist):
    if possible_setups[milklist[0]][milklist[1]][milklist[2]] == 0:
        possible_setups[milklist[0]][milklist[1]][milklist[2]] = 1
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                tempmilk = [milklist[0], milklist[1], milklist[2]]
                pourMilk(tempmilk, i, j)
                milkSolve(tempmilk)

milkSolve(start)

diffs = set()

for c in range(capacity[2] + 1):
    for b in range(capacity[1] + 1):
        if possible_setups[0][b][c] == 1:
            diffs.add(c)
diffs = list(diffs)
diffs.sort()
#print(diffs)
fout = open("milk3.out", "w")
for item in diffs[:-1]:
    fout.write(str(item) + " ")
fout.write(str(diffs[-1]) + "\n")

"""with open("milk3.in", "r") as fin:
    A, B, C = map(int, fin.readline().split())
#print(A)
#print(B)
#print(C)
if A < B:
    buckcap = [A, B, C]
elif B < A:
    buckcap = [B, A, C]
else:
    buckcap = [A, B, C]
print(buckcap)
diffs = []
if A == B and B == C:
    diffs.append(0)
elif max(buckcap) == C:
    for i in range(-1 * (C // buckcap[0]), (C // buckcap[0]) + 1):
        for j in range(-1 * (C // buckcap[1]), (C // buckcap[1]) + 1):
            for k in range(-1 * (C // (buckcap[2] - buckcap[1])), (C // (buckcap[2] - buckcap[1])) + 1):
                #print(i, j, k)
                diff = buckcap[0] * i + buckcap[1] * j + (buckcap[2] - buckcap[1]) * k
                #print(diff)
                if -1 * C < diff < 0:
                    diff = diff % C
                    #print(diff)
                if (C - A) <= diff and (C - B) <= diff and diff <= C:
                    #print(diff)
                    diffs.append(diff)
else:
    pass
diffs.append(C)
diffs = list(set(diffs))
print(diffs)
#print C // A
#print C // B

fout = open("milk3.out", "w")
for i in range(len(diffs) - 1):
    fout.write(str(diffs[i]) + " ")
fout.write(str(diffs[-1]))
fout.write("\n")
fout.close()"""
