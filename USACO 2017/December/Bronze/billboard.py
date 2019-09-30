fin = open("billboard.in", "r")

class Billboard(object):
    def __init__(self, coordli):
        self.x1 = coordli[0]
        self.y1 = coordli[1]
        self.x2 = coordli[2]
        self.y2 = coordli[3]
    def area(self):
        return abs((self.x1 - self.x2) * (self.y1 - self.y2))
    def inside(self, x, y):
        if self.x1 <= x <= self.x2 and self.x1 <= x + 1 <= self.x2:
            if self.y1 <= y <= self.y2 and self.y1 <= y + 1 <= self.y2:
                return True
        return False
    def returnx(self):
        return [self.x1, self.x2]
    def returny(self):
        return [self.y1, self.y2]

ba = Billboard(map(int, fin.readline().split()))
bb = Billboard(map(int, fin.readline().split()))
tt = Billboard(map(int, fin.readline().split()))

"""xs = []
ys = []
xs.extend(ba.returnx())
xs.extend(bb.returnx())
xs.extend(tt.returnx())
ys.extend(ba.returny())
ys.extend(bb.returny())
ys.extend(tt.returny())"""

cells = ba.area() + bb.area()

if (ba.x1 < tt.x1 < tt.x2 < ba.x2 and ba.y1 < tt.y1 < tt.y2 < ba.y2) or (bb.x1 < tt.x1 < tt.x2 < bb.x2 and bb.y1 < tt.y1 < tt.y2 < bb.y2):
    cells -= tt.area()
else:
    for i in range(tt.x1, tt.x2):
        for j in range(tt.y1, tt.y2):
            if ba.inside(i, j) or bb.inside(i, j):
                cells -= 1
#print(cells)

fout = open("billboard.out", "w")
fout.write(str(cells) + "\n")
fout.close()
