fin = open("outofplace.in", "r")

cows = int(fin.readline())
order = []
for i in range(cows):
    order.append(int(fin.readline()))
sortorder = sorted(order)

def compare(l1, l2):
    for i in range(0, min(len(l1), len(l2))):
        if l1[i] != l2[i]:
            return i

ind = compare(order, sortorder)

#print(order)
#print(sortorder)

swaps = -1
for i in range(0, cows):
    if order[i] != sortorder[i]:
        swaps += 1

fout = open("outofplace.out", "w")
fout.write(str(swaps) + "\n")
fout.close()
