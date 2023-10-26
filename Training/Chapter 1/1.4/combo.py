"""
ID: ********
LANG: PYTHON2
TASK: combo
"""

with open("combo.in", "r") as fin:
    N = int(fin.readline()) #numbering on dials
    farmlock = list(map(int, fin.readline().split()))
    masterlock = list(map(int, fin.readline().split()))
#print N
#print farmlock
#print masterlock

def lockRegulator(n): #given a number makes it fit within dial numbering
    if n <= 0:
        return n + N
    if n > N:
        return n - N
    else:
        return n

nr = set(range(1, N + 1))
dials = []
#print nr
for i in range(3):
    fr = set(map(lockRegulator, range(farmlock[i]-2, farmlock[i]+3))) & nr  # set of dials near farmer's key
    mr = set(map(lockRegulator, range(masterlock[i]-2, masterlock[i]+3))) & nr  # set of dials near master's key
    #print fr
    #print mr
    dials.append(len(fr & mr))  # set of dials that suit both patterns
    #print dials
result = 2*(min(N,5)**3) - dials[0]*dials[1]*dials[2]
"""
min(N, 5) ** 3 --> dial settings that work
2 * min(N, 5) ** 3 --> combined of famer and master, w/ repeats
- dials[0]*dials[1]*dials[2] --> subtracts combos that fit both
"""
fout = open("combo.out", "w")
fout.write(str(result) + "\n")
fout.close()
