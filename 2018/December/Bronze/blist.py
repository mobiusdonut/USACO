fin = open("blist.in", "r")
buckli = [0 for i in range(1001)]

n = int(fin.readline())

minday = 1000
maxday = 1
for i in range(n):
    cowli = map(int, fin.readline().split())
    minday = min(minday, cowli[0])
    maxday = max(maxday, cowli[1])
    for i in range(cowli[0], cowli[1] + 1):
        buckli[i] += cowli[2]

#print(buckli[minday:maxday + 1])

fout = open("blist.out", "w")
fout.write(str(max(buckli)) + "\n")
fout.close()
