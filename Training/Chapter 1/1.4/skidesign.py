"""
ID: ********
LANG: PYTHON3
TASK: skidesign
"""

with open("skidesign.in", "r") as fin:
    hills = int(fin.readline())
    elevations = []
    for i in range(hills):
        elevations.append(int(fin.readline()))
#print(hills)
#print(elevations)
elevations.sort()
#print(elevations)
price_list = []
for start in range(min(elevations), max(elevations) - 17): #range is the list of minimum heights of the hills
    end = start + 17 #start is minimum height, end is maximum height
    price = 0
    for hill in elevations:
        if hill > end:
            price += (hill - end) ** 2
        elif hill < start:
            price += (start - hill) ** 2
    price_list.append(price)

if not price_list:
    price_list = [0]
minprice = min(price_list)
fout = open("skidesign.out", "w")
fout.write(str(minprice) + "\n")
fout.close()
