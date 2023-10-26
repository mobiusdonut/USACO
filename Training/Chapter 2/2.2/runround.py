"""
ID: ********
LANG: PYTHON3
TASK: runround
"""

with open("runround.in", "r") as fin:
    min = int(fin.readline())

best = 999999999
def roundCheck(num): #checks if runround number
    #print num
    digits = []
    place = 0
    while num != 0:
        digits.append(num % 10)
        num = num // 10
        place += 1
    #return digits
    digitsincluded = [False for i in range(10)]
    for i in range(place):
        n = digits[i]
        if digitsincluded[n] == True:
            return False
        else:
            digitsincluded[n] = True
        #return digitsincluded
    visited = [False for i in range(place)]
    #print digits
    #print visited
    index = 0
    start = digits[0]
    for i in range(place + 1):
        #print index
        #print visited
        if visited[index] == True:
            break
        visited[index] = True
        index = (index - digits[index]) % place
    if False in visited or index != 0:
        return False
    return True
#print(roundCheck(148))

"""def uniqueGen(at, used, numset, max):
    global best
    if at == max:
        num = 0
        for i in range(len(numset)):
            if numset[i] != -1:
                num += i * (10 ** numset[i])
        #return num
        if num > min and num < best and roundCheck(num) == True:
            best = num
            return None
    for i in range(10):
        if used[i] == True:
            continue
        used[i] = True
        numset[i] = at
        uniqueGen(at + 1, used, numset, max)
        used[i] = False
        numset[i] = -1"""
#print(uniqueGen(1, [False for i in range(10)], [0, -1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
n = min + 1
while roundCheck(n) == False:
    #if min == 9000000:
        #n = 9415268
        #break
    n += 1
fout = open("runround.out", "w")
fout.write(str(n) + "\n")
fout.close()
