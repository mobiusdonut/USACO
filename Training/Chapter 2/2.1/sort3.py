"""
ID: ********
LANG: PYTHON3
TASK: sort3
"""

unsorted = []
with open("sort3.in", "r") as fin:
    N = int(fin.readline())
    for i in range(N):
        unsorted.append(int(fin.readline()))
sorted = sorted(unsorted)
#print unsorted
#print sorted

mis12 = 0
mis21 = 0
mis13 = 0
mis31 = 0
mis23 = 0
mis32 = 0

for i in range(N):
    if sorted[i] == 1 and unsorted[i] == 2:
        mis12 += 1
    if sorted[i] == 2 and unsorted[i] == 1:
        mis21 += 1
    if sorted[i] == 1 and unsorted[i] == 3:
        mis13 += 1
    if sorted[i] == 3 and unsorted[i] == 1:
        mis31 += 1
    if sorted[i] == 2 and unsorted[i] == 3:
        mis23 += 1
    if sorted[i] == 3 and unsorted[i] == 2:
        mis32 += 1
#print mis12
#print mis21
#print mis13
#print mis31
#print mis23
#print mis32

moves = (min(mis12, mis21)) + (min(mis13, mis31)) + (min(mis23, mis32)) + (2*(max(mis12,mis21)-min(mis12,mis21)))
fout = open("sort3.out", "w")
fout.write(str(moves) + "\n")
fout.close()
