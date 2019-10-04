"""
ID: kripaki1
LANG: PYTHON3
TASK: fracdec
"""

fin = open("fracdec.in", "r")
numer, denom = map(int, fin.readline().split())
print(numer, denom)

fracstring = ""

fracstring += str(numer//denom) + "."

numer %= denom

if numer == 0:
    fracstring += "0"

else:
    repeat = -1
    visited = {}
    frac = []
    counter = 0
    while numer:
        #print(numer)
        numer *= 10
        if numer in visited:
            repeat = visited[numer]
            numer = 0
        else:
            visited[numer] = counter
            frac.append(numer//denom)
            numer %= denom
            counter += 1
        #print(frac)
        #print(repeat)
        #print(visited)
    replen = len(visited) - repeat
    if repeat == -1:
        fracstring += "".join(map(str, frac))
    else:
        fracstring += "".join(map(str, frac[:repeat]))
        fracstring += "("
        fracstring += "".join(map(str, frac[repeat:]))
        fracstring += ")"
    #print(fracstring)

fout = open("fracdec.out", "w")

if len(fracstring) <= 76:
    fout.write(fracstring)
else:
    for i in range(len(fracstring)//76):
        fout.write(fracstring[i * 76: (i + 1) * 76] + "\n")
    if len(fracstring) % 76 != 0:
        fout.write(fracstring[(i + 1) * 76:])
fout.write("\n")
fout.close()
