
class point:
  def __str__(self):
    return f"({self.x}, {self.y})"
  def get_x (self):
    return self.x
  def get_y (self):
    return self.y

  def get_coords (self):
    return (self.x, self.y)

p = point(0,2)
print(p.get_x())
print(p.get_y())
print(p.get_coords())


