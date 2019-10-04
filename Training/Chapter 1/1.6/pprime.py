"""
ID: kripaki1
LANG: PYTHON3
TASK: pprime
"""

with open("pprime.in", "r") as fin:
    min, max = map(int, fin.readline().split())
print(min, max)

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

def primePal(min, max):
    primepal = []
    if min <= 2 and max >= 2:
        primepal.append(2)
    if min <= 5 and max >= 5:
        primepal.append(5)
    if min <= 7 and max >= 7:
        primepal.append(7)
    if max < 11:
        return primepal
    for d1 in range(1, 10, 2):
        pal = 10 * d1 + d1
        if isPrime(pal):
            primepal.append(pal)
    if max < 101:
        return primepal
    for d1 in range(1, 10, 2):
        for d2 in range(0, 10):
            pal = 100 * d1 + 10 * d2 + d1
            if isPrime(pal):
                primepal.append(pal)
                print(pal)
            pal = 1000 * d1 + 100 * d2 + 10 * d2 + d1
            if isPrime(pal):
                primepal.append(pal)
                print(pal)
    if max < 10001:
        return primepal
    for d1 in range(1, 10, 2):
        for d2 in range(0, 10):
            for d3 in range(0, 10):
                pal = 10000 * d1 + 1000 * d2 + 100 * d3 + 10 * d2 + d1
                if isPrime(pal):
                    primepal.append(pal)
                pal = 100000 * d1 + 10000 * d2 + 1000 * d3 + 100 * d3 + 10 * d2 + d1
                if isPrime(pal):
                    primepal.append(pal)
    if max < 1000001:
        return primepal
    for d1 in range(1, 10, 2):
        for d2 in range(0, 10):
            for d3 in range(0, 10):
                for d4 in range(0, 10):
                    pal = 1000000 * d1 + 100000 * d2 + 10000 * d3 + 1000 * d4 + 100 * d3 + 10 * d2 + d1
                    if isPrime(pal):
                        primepal.append(pal)
                    pal = 10000000 * d1 + 1000000 * d2 + 100000 * d3 + 10000 * d4 + 1000 * d4 + 100 * d3 + 10 * d2 + d1
                    if isPrime(pal):
                        primepal.append(pal)
    primepal.sort()
    return primepal

primepalindromes = primePal(min, max)

fout = open("pprime.out", "w")
for item in primepalindromes:
    if item >= min and item <= max:
        fout.write(str(item) + "\n")
fout.close()
