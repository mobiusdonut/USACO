"""
ID: kripaki1
LANG: PYTHON3
TASK: prefix
"""

fin = open("prefix.in", "r")

prims = ["pl"]

while not "." in prims[-1]:
    prims.extend(fin.readline().split())

prims.remove("pl")
prims.remove(".")
prims = sorted(prims, key=len)[::-1]

print(prims)

seq = fin.read().split("\n")
#print seq
seq = "".join(seq)
seqlen = len(seq)
#print seqlen
fin.close()

if seqlen >= 100000:
    maxa = 0
    maxb = 0

    prims2 = prims[:]
    prims2.append("")

    for prim in prims:
        for prim2 in prims2:
            primcom = prim + prim2
            if len(primcom) == primcom.count("A"):
                maxa = len(prims[0])
            if len(primcom) == primcom.count("B"):
                maxb = len(prims[0])
            else:
                maxa = max(maxa, primcom.count("A"))
                maxb = max(maxb, primcom.count("B"))

    print(maxa, maxb)
    aindex = -1
    bindex = -1

    try:
        aindex = seq.index("A" * (maxa + 1))
        bindex = seq.index("B" * (maxb + 1))
    except:
        print("Not Found")

    print(aindex, bindex)

    maxlen = 0

    if bindex > aindex and bindex != 0:
        maxlen = bindex
        for prim in prims:
            if prim.endswith("B"):
                if seq[bindex - prim.index("B"):bindex - prim.index("B") + len(prim)] == prim:
                    maxlen = max(maxlen, bindex + len(prim) - prim.index("B"))
    elif aindex > bindex and aindex != 0:
        maxlen = aindex
        for prim in prims:
            if prim.endswith("A"):
                if seq[aindex - prim.index("A"):aindex - prim.index("A") + len(prim)] == prim:
                    maxlen = max(maxlen, aindex + len(prim) - prim.index("A"))

    print(maxlen)

else:
    match_str_len = [0 for i in range(len(seq) + 1)]

    #print("b")

    for i in range(len(seq) - 1, -1, -1):
        for prim in prims:
            if i + len(prim) <= seqlen and seq[i:i + len(prim)] == prim:
                match_str_len[i] = max(match_str_len[i], match_str_len[i + len(prim)] + len(prim))
                #print(match_str_len[i])

    #print("c")

    #print match_str_len
    maxlen = match_str_len[0]
print(maxlen)
fout = open("prefix.out", "w")
fout.write(str(maxlen) + "\n")
fout.close()
