"""
ID: kripaki1
LANG: PYTHON2
TASK: crypt1
"""

with open("crypt1.in", "r") as fin:
    N = int(fin.readline())
    digits = fin.readline().split()
    #digit_set = set(digits)
    #print N
    #print digits

"""
FORMAT:
          a b c     <-- number 'abc'
        x   d e     <-- number 'de'; the 'x' means 'multiply'
     -----------
p1      * * * *     <-- product of e * abc; first star might be 0 (absent)
p2    * * * *       <-- product of d * abc; first star might be 0 (absent)
     -----------
      * * * * *     <-- sum of p1 and p2 (e*abc + 10*d*abc) == de*abc
"""
solution_count = 0
for i in range(100, 1000): #abc
    for j in range (10, 100): #de
        concat = str(i) + str(j) #for checking if digits in i and j
        product = str(i * j) #for checking if digits in product of i and j
        pp1 = str(i * (j % 10)) #for checking if digits in first partial product
        pp2 = str(i * (j // 10)) #for checking if digits in second partial product
        fullconcat = concat + product + pp1 + pp2
        if all(char in digits for char in fullconcat):
            if len(product) == 4 and len(pp1) == 3 and len(pp2) == 3:
                solution_count += 1
print(solution_count)
fout = open("crypt1.out", "w")
fout.write(str(solution_count) + "\n")
fout.close()
