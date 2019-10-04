"""
ID: kripaki1
LANG: PYTHON2
TASK: namenum
"""
def charToNum(c):
    if ord(c) < ord('Q'):
        return str((ord(c) - 65)//3 + 2)
    else:
        return str((ord(c) - 66)//3 + 2)

with open('dict.txt','r') as namedict:
    name_list = namedict.read().split('\n')

serials = [''.join(list(map(charToNum, name))) for name in name_list]
#serials = [list(map(charToNum, name)) for name in name_list]
#print type(serials)
#print serials
with open("namenum.in", "r") as namenumin:
    serial = namenumin.read()[:-1]

i = -1
o = ""
while serial in serials[i+1: ]:
    i = serials.index(serial, i+1)
    o += name_list[i] + "\n"
if o == "":
    o = "NONE\n"
with open("namenum.out", "w") as namenumout:
    namenumout.write(o)
#print o
