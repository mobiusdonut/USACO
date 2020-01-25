fin = open("mixmilk.in", "r")
acap, acurr = map(int, fin.readline().split())
bcap, bcurr = map(int, fin.readline().split())
ccap, ccurr = map(int, fin.readline().split())

class Bucket(object):
    def __init__(self, cap, curr, name):
        self.cap = cap
        self.curr = curr
        self.name = name
    def __repr__(self):
        return ("bucket " + str(self.name) + " of capacity " + str(self.cap) + " with " + str(self.curr))
    def pour(self, b2):
        #print(self, b2)
        if b2.cap - b2.curr >= self.curr:
            b2.curr = b2.curr + self.curr
            self.curr = 0
        else:
            self.curr = self.curr - (b2.cap - b2.curr)
            b2.curr = b2.cap

a = Bucket(acap, acurr, 1)
b = Bucket(bcap, bcurr, 2)
c = Bucket(ccap, ccurr, 3)
x = 0
#print(x, a.curr, b.curr, c.curr)

for i in range(33):
    a.pour(b)
    x += 1
    #print(x, a.curr, b.curr, c.curr)
    b.pour(c)
    x += 1
    #print(x, a.curr, b.curr, c.curr)
    c.pour(a)
    x += 1
    #print(x, a.curr, b.curr, c.curr)
a.pour(b)
#print(x, a.curr, b.curr, c.curr)

n = [a.curr, b.curr, c.curr]
fout = open("mixmilk.out", "w")
for item in n:
    fout.write(str(item) + "\n")
fout.close()
