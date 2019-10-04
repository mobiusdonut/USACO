"""
ID: kripaki1
LANG: PYTHON2
TASK: transform
"""

with open("transform.in", "r") as transformin:
    N = int(transformin.readline())
    before = []
    for i in range(N):
        before.append(list(transformin.readline()[:-1]))
    after = []
    for i in range(N):
        after.append(list(transformin.readline()[:-1]))
    #print before
    #print after

def rotateMatrix(m):
    #rotates argument nested list by 90 degrees right
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(m[N - j - 1][i])
        result.append(row)
    return result
def reflectMatrix(m):
    #reflects argument nested list across y axis
    result = []
    return [x[::-1] for x in m]
#print before
#print rotateMatrix(before)
#print reflectMatrix(before)
num = 7
bef = before
for i in range(1, 4):
    bef = rotateMatrix(bef)
    if bef == after:
        num = i
        break
else:
    if reflectMatrix(before) == after:
        num = 4
    else:
        bef = reflectMatrix(before)
        for i in range(3):
            bef = rotateMatrix(bef)
            if bef == after:
                num = 5
                break
        else:
            if before == after:
                num = 6
            else:
                num = 7
with open('transform.out','w') as transformout:
    transformout.write(str(num)+'\n')
