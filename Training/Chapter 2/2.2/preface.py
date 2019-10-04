"""
ID: kripaki1
LANG: PYTHON3
TASK: preface
"""

count = [0 for i in range(7)]
chars = ['I','V','X','L','C','D','M']
def romanize(n):
    converter = [["","I","II","III","IV","V","VI","VII","VIII","IX"], ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
    ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"], ["","M","MM","MMM","MMMM","MMMMM","vM","vMM","vMMM","Mx"],
    ["","x","xx","xxx","xl","l","lx","lxx","lxxx","xc"], ["","c","cc","ccc","cd","d","dc","dcc","dccc","cm"],
    ["","m","mm","mmm","","","","","",""]]

    roman = ""

    i = 0
    while n > 0:
        digit = n % 10
        roman = converter[i][digit] + roman
        i += 1
        n = n // 10
    return roman
def romanCounter(romanstr):
    for j in range(len(romanstr)):
        for k in range(len(chars)):
            if romanstr[j] == chars[k]:
                count[k] += 1

with open("preface.in", "r") as fin:
    N = int(fin.readline())

for num in range(1, N + 1):
    romanCounter(romanize(num))
#print count

fout = open("preface.out", "w")

for i in range(7):
    if count[i] != 0:
        fout.write(chars[i] + " " + str(count[i]) + "\n")

fout.close()
