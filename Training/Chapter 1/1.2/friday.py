"""
ID: ********
LANG: PYTHON2
TASK: friday
"""

fin = open("friday.in", "r")
n = int(fin.readline())
#calculates days per month in all months
def DaysPerMonth(year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days[1] += 1
    return days

def Thirteens(n):
    total = 0
    #total days passed
    count = [0, 0, 0, 0, 0, 0, 0]
    #separation of 13s by day of week
    for i in range (1900, 1900 + n):
        days = DaysPerMonth(i)
        for j in range(12):
            count[(total + 13) % 7] += 1
            total += days[j]
    return count

count = Thirteens(n)
fout = open("friday.out", "w")
fout.write(" ".join([str(i) for i in count[-1:] + count[:-1]]) + "\n")
#move around counts to offset for jan 1 being monday
fout.close()
