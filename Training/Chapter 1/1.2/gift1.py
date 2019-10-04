"""
ID: kripaki1
LANG: PYTHON2
TASK: gift1
"""
giftin = open ("gift1.in", "r")
people_count = int(giftin.readline().strip())
name_list = []
money = {}
for i in range(people_count):
    person = giftin.readline().strip()
    name_list.append(person)
    money[person] = 0

while True:
    giver = giftin.readline().strip()
    if not giver:
        break
    much, num = (int(a.strip()) for a in giftin.readline().split())
    giftees = []
    for person in range(num):
        giftees.append(giftin.readline().strip())
    if 0 in [much, num]:
        continue
    money[giver] -= much - much % num
    for person in giftees:
        money[person] += much // num

with open("gift1.out", "w") as giftout:
    for name in name_list:
        giftout.write(name + " " + str(money[name]) + "\n")
giftout.close()
