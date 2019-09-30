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
    def __repr__(self):
        return(" x1: " + str(self.x1) + " y1: " + str(self.y1) + " x2: " + str(self.x2) + " y2: " + str(self.y2))

bl = Billboard(map(int, fin.readline().split()))
bc = Billboard(map(int, fin.readline().split()))

cells = 0

print(bl)
print(bc)

if bc.inside(bl.x1, bl.y1 - 1) and bc.inside(bl.x2 - 1, bl.y1 - 1) and bc.inside(bl.x2 - 1, bl.y2) and bc.inside(bl.x1, bl.y2):
    cells = 0
else:
    if bc.x1 <= bl.x1:
        if bc.x2 >= bl.x2:
            if bc.y1 >= bl.y1:
                if bc.y2 <= bl.y2:
                    cells = 0
                    print("a")
                else:
                    cells = abs((bc.y1 - bl.y2) * (bl.x1 - bl.x2))
                    print("b")
            else:
                if bc.y2 <= bl.y2:
                    cells = abs((bc.y1 - bl.y2) * (bl.x1 - bl.x2))
                    print("c")
                else:
                    cells = 0
                    print("d")
        else:
            if bc.y1 <= bl.y1:
                if bc.y2 >= bl.y2:
                    cells = abs((bl.y1 - bl.y2) * (bl.x1 - bc.x2))
                    print("e")
                else:
                    cells = 0
                    print("f")
            else:
                cells = 0
                print("g")
    else:
        if bc.x2 >= bl.x2:
            if bc.y1 >= bl.y1:
                if bc.y2 <= bl.y2:
                    cells = abs((bl.y1 - bl.y2) * (bc.x1 - bl.x2))
                    print("h")
                else:
                    cells = 0
                    print("i")
            else:
                cells = 0
                print("j")
        else:
            if bc.y1 >= bl.y1:
                if bc.y2 <= bl.y2:
                    cells = abs((bl.y1 - bl.y2) * (bl.x1 - bc.x2))
                    print("k")
                else:
                    cells = 0
                    print("l")
            else:
                cells = 0
                print("m")

    cells = bl.area() - cells
print(cells)

fout = open("billboard.out", "w")
fout.write(str(cells) + "\n")
fout.close()
