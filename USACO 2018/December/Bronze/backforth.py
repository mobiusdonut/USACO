fin = open("backforth.in", "r")
b1 = map(int, fin.readline().split())
b2 = map(int, fin.readline().split())
barn1 = 1000
barn2 = 1000
vals = set()

def carry(day):
    global barn1, barn2
    #print(barn1, barn2)
    if day == 6:
        vals.add(barn1)
    elif day % 2 == 0:
        for item in set(b1):
            b1.remove(item)
            b2.append(item)
            barn1 -= item
            barn2 += item
            carry(day + 1)
            barn2 -= item
            barn1 += item
            b2.remove(item)
            b1.append(item)
    elif day % 2 == 1:
        for item in set(b2):
            b2.remove(item)
            b1.append(item)
            barn2 -= item
            barn1 += item
            carry(day + 1)
            barn1 -= item
            barn2 += item
            b1.remove(item)
            b2.append(item)

carry(2)
#print(vals)

fout = open("backforth.out", "w")
fout.write(str(len(vals)) + "\n")
fout.close()
