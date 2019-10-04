"""
ID: kripaki1
LANG: PYTHON2
TASK: dualpal
"""

def baseConverter(n, base):
    leftdigit = 0
    result = []
    while n >= base**leftdigit:
        leftdigit += 1

    for i in reversed(range(leftdigit)):
        d = n // (base**i)
        if d < 10:
            d = str(d)
        else:
            d = chr(ord('A')+d-10)
        result.append(d)
        n = n % (base**i)
        #print n

    return ''.join(result)

#print type(baseConverter(15, 2))
with open('dualpal.in','r') as fin:
    N, S = map(int, fin.readline().split())
#print N
#print S
b = S

result = []
while len(result) < N:
    b += 1 #number being checked
    c = 0 #count of bases in which it is a palindrome
    for i in range(2, 11):
        bbase = baseConverter(b, i)

        if bbase == bbase[::-1]:
            #print b, bbase
            c += 1
        if c == 2:
            result.append(b)
            break
    #if b >= 10000:
        #break
#print result
fout = open("dualpal.out", "w")
for item in result:
    fout.write(str(item) + "\n")
fout.close()
