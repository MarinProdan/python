class point:
    x = 0
    y = 2
#print(point.x,point.y)
A = point()
#print(A.x,A.y)
point.x = 5
B = point()
print(point.x,A.x,B.x)
C=point()
point.x = 57
print(point.x,A.x,B.x,C.x)

class Point:
    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord
o = Point()
p = Point(1, 2)
q = Point(3, 5)

print (f"({o.x}, {o.y})")
print(f"({p.x}, {p.y})")
print (f"({q.x}, {q.y})")


class Point:
    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord

    def __str__(self):
        return f"({self.x}, {self.y})"
p= Point(0,2)
q = Point(3,5)
print(p)
print(q)


class point3:
 def set_x(self, new_xcoord):
    self.x = new_xcoord
 def set_y(self, new_ycoord):
    self.y = new_ycoord
 def set_coords(self, new_xcoord, new_ycoord):
    self.x = new_xcoord
    self.y = new_ycoord
p = point3(3,0)
print(p)


p.set_x(8)
print(p)

p.set_y(4)
print(p)

p.set_coords(5,6)
print(p)
