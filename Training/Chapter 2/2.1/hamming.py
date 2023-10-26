"""
ID: ********
LANG: PYTHON3
TASK: hamming
"""

with open("hamming.in", "r") as fin:
    n, b, d = map(int, fin.readline().split())
#print(n)
#print(b)
#print(d)

#calculates num of differences between 2 sequences
def distance(bitseq1, bitseq2):
    diffs = 0
    #print(bitseq1)
    #print(bitseq2)
    diffcounter = bitseq1 ^ bitseq2
    while diffcounter > 0:
        #print(diffcounter)
        diffs += (diffcounter & 1)
        diffcounter = diffcounter >> 1
    return diffs
def hamsolve(n, b, d):
    words = []
    p = 0
    for word in range(1 << b + 1):
        wordcheck = True
        for item in words:
            if distance(word, item) < d:
                wordcheck = False
                break
        if wordcheck == True:
            words.append(word)
            p += 1
        if p == n:
            break
    return words
#print(distance(0b1010100101, 0b1001101001))
#print bin(0b100 >> 1)
codewords = hamsolve(n, b, d)

fout = open("hamming.out", "w")
count = 1
for word in codewords[:-1]:
    if count != 10:
        fout.write(str(word) + " ")
        count += 1
    elif count == 10:
        fout.write(str(word) + "\n")
        count = 1
fout.write(str(codewords[-1]) + "\n")
fout.close()
