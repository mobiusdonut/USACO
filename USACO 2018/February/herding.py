fin = open("herding.in", "r")

def max0s(arr):
    count = 0
    result = 0

    for i in range(0, len(arr)):
        if (arr[i] == 1):
            count = 0
        else:
            count+= 1
            result = max(result, count)
    return result

n = int(fin.readline())
cowli = []
maxi = 0
mini = 1000000000
for i in range(n):
    x = int(fin.readline())
    cowli.append(x)
    maxi = max(maxi, x)
    mini = min(mini, x)
cows = [0 for i in range(maxi + 1)]
for item in cowli:
    cows[item] = 1
#print(cows)
cowsstr = str(cows)

maxres = max0s(cows[mini:])
maxres = min(maxres, n - 2)
minres = 0
for i in range(n - 2, maxres):
    if "0" * i in cowsstr:
         minres = i
         break
#print(minres, maxres)

fout = open("herding.out", "w")
fout.write(str(minres) + "\n")
fout.write(str(maxres) + "\n")
fout.close()
