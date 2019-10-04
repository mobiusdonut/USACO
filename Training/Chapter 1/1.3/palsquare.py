"""
ID: kripaki1
LANG: PYTHON2
TASK: palsquare
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
#print baseConverter(1200, 16)
with open("palsquare.in", "r") as fin:
    B = int(fin.readline())
#print B

pal_dict = []
square_dict = []
for i in range(0, 301):
    num = baseConverter(i, B)
    numsquare = baseConverter(i ** 2, B)
    if numsquare == numsquare[::-1]:
        pal_dict.append(num)
        square_dict.append(numsquare)
        #print num + " True"
    #else:
        #print num + "False"
pal_dict.remove("")
square_dict.remove("")
#print pal_dict
#print square_dict
fout = open("palsquare.out", "w")
for i in range(len(pal_dict)):
    fout.write(pal_dict[i] + " " + square_dict[i] + "\n")
fout.close()
