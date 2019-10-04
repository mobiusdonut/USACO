"""
ID: kripaki1
LANG: PYTHON3
TASK: ttwo
"""

fin = open("ttwo.in", "r")

field = []
for i in range(10):
    fieldrow = []
    row = list(fin.readline())[:-1]
    print(row)
    for item in row:
        if item == "C":
            #print("Cows found")
            cows = [i, row.index("C"), 0]
        if item == "F":
            #print("Farmer found")
            farmer = [i, row.index("F"), 0]
        fieldrow.append(item)
    field.append(fieldrow)
fin.close()


print(farmer)
print(cows)

n = 0

while farmer[0] != cows[0] or farmer[1] != cows[1]:
    n += 1
    if farmer[2] == 0:
        if farmer[0] == 0:
            farmer[2] = 1
        elif field[farmer[0] - 1][farmer[1]] == "*":
            farmer[2] = 1
        else:
            farmer[0] -= 1
    elif farmer[2] == 1:
        if farmer[1] == 9:
            farmer[2] = 2
        elif field[farmer[0]][farmer[1] + 1] == "*":
            farmer[2] = 2
        else:
            farmer[1] += 1
    elif farmer[2] == 2:
        if farmer[0] == 9:
            farmer[2] = 3
        elif field[farmer[0] + 1][farmer[1]] == "*":
            farmer[2] = 3
        else:
            farmer[0] += 1
    elif farmer[2] == 3:
        if farmer[1] == 0:
            farmer[2] = 0
        elif field[farmer[0]][farmer[1] - 1] == "*":
            farmer[2] = 0
        else:
            farmer[1] -= 1
    if cows[2] == 0:
        if cows[0] == 0:
            cows[2] = 1
        elif field[cows[0] - 1][cows[1]] == "*":
            cows[2] = 1
        else:
            cows[0] -= 1
    elif cows[2] == 1:
        if cows[1] == 9:
            cows[2] = 2
        elif field[cows[0]][cows[1] + 1] == "*":
            cows[2] = 2
        else:
            cows[1] += 1
    elif cows[2] == 2:
        if cows[0] == 9:
            cows[2] = 3
        elif field[cows[0] + 1][cows[1]] == "*":
            cows[2] = 3
        else:
            cows[0] += 1
    elif cows[2] == 3:
        if cows[1] == 0:
            cows[2] = 0
        elif field[cows[0]][cows[1] - 1] == "*":
            cows[2] = 0
        else:
            cows[1] -= 1

    print(n)
    print(farmer)
    print(cows)

    if n >= 16000:
        n = 0
        break

fout = open("ttwo.out", "w")
fout.write(str(n) + "\n")
fout.close()
