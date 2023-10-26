"""
ID: ********
LANG: PYTHON3
TASK: subset
"""

with open("subset.in", "r") as fin:
    N = int(fin.readline())
sum = 0
for i in range(1, N + 1):
    sum += i
#print sum
sum_array = [[-1 for i in range(sum + 1)] for i in range(N)]
#print(sum_array)
goal = sum / 2
def summer(num, sum):
    global goal
    if sum == goal:
        #print "Goal Reached"
        #print sum
        return 1
    if num == N:
        return 0
    if sum_array[num][sum] != -1:
        return sum_array[num][sum]
    ans = summer(num + 1, sum + num + 1) + summer(num + 1, sum)
    #print
    #print num
    #print sum
    #print ans
    #print
    sum_array[num][sum] = ans
    return ans
if sum % 2 == 1:
    partitions = 0
else:
    partitions = summer(0, 0)/2
#print(sum_array)
print(partitions)

fout = open("subset.out", "w")
fout.write(str(int(partitions)) + "\n")
fout.close()
