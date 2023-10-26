"""
ID: ********
LANG: PYTHON3
TASK: sprime
"""

#prime_list = []
def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    root = num ** 0.5
    for div in range(2, int(root) + 1):
        if num % div == 0:
            return False
    return True

def makePrimes(remainingDigs, orgprime, file):
    if remainingDigs == 0:
        #print orgprime
        file.write(str(orgprime) + "\n")
    for i in range(orgprime * 10 + 1, orgprime * 10 + 10):
        if isPrime(i) == True:
            makePrimes(remainingDigs - 1, i, file)

with open("sprime.in", "r") as fin:
    length = int(fin.readline())

    #prime_list = prime_list.sort()
#print(prime_list)

fout = open("sprime.out", "w")
#for item in prime_list:
    #fout.write(str(item) + "\n")
makePrimes(length, 0, fout)
fout.close()
