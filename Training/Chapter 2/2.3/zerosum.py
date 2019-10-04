"""
ID: kripaki1
LANG: PYTHON3
TASK: zerosum
"""

fin = open("zerosum.in", "r")
n = int(fin.readline())
fin.close()

seq = [0] * (2 * n - 1)
for i in range(n):
    seq[i * 2] = i + 1
#print seq

seqlist = []

def seqset(seqe, depth):
    #print depth
    if depth == 2 * n - 1:
        seqlist.append(seqe[:])
        return None
    if depth % 2 == 0:
        seqset(seqe, depth + 1)
    else:
        seqe[depth] = " "
        seqset(seqe, depth + 1)
        seqe[depth] = "+"
        seqset(seqe, depth + 1)
        seqe[depth] = "-"
        seqset(seqe, depth + 1)

seqset(seq, 0)
#print seqlist
#print len(seqlist)

checkseqs = []

def zerosumcheck(sequence):
    #global n
    total = 0
    #b = seq[0]
    #print sequence
    seq2 = sequence[:]
    while " " in seq2:
        #print seq2.index(" ")
        seq2[seq2.index(" ") - 1] = seq2[seq2.index(" ") - 1] * 10 + seq2[seq2.index(" ") + 1]
        del seq2[seq2.index(" ") + 1]
        del seq2[seq2.index(" ")]
        #print seq2
    total = eval("".join(map(str, seq2)))
    if total == 0:
        return True
    else:
        return False
    """for i in range(1, 2 * n - 1, 2):
        #print i
        #print seq[i]
        if sequence[i] == 0: # " "
            total += sequence[i - 1] * 10 + sequence[i + 1]
        elif sequence[i] == 1: # "+"""

seqs = []

for sequence in seqlist:
    if zerosumcheck(sequence):
        seqs.append("".join(map(str, sequence)))

fout = open("zerosum.out", "w")
for seque in seqs:
    fout.write(seque + "\n")
fout.close()
#print(zerosum(1+2-3+4-5-6+7))
