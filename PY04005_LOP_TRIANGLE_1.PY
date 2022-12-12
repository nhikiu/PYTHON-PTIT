import math

class Point:
  def __init__(self, tu, mau):
    self.tu = tu
    self.mau = mau
  def distance(self, point):
    return math.sqrt((self.tu - point.tu) ** 2 + (self.mau - point.mau) ** 2)

class Triangle:
  def __init__(self, p1, p2, p3):
    self.p1 = p1
    self.p2 = p2
    self.p3 = p3
  def valid(self):
    a = self.p1.distance(self.p2)
    b = self.p2.distance(self.p3)
    c = self.p3.distance(self.p1)
    if a + b <= c or b + c <= a or c + a <= b:
      return 'INVALID'
    return '{:.3f}'.format(a + b + c)

inp = []
t = int(input())
for case in range(t):
  inp += [float(i) for i in input().split()]
i = 0
for case in range(t):
  triangle = Triangle(Point(inp[i], inp[i + 1]), Point(inp[i + 2], inp[i + 3]), Point(inp[i + 4], inp[i + 5]))
  print(triangle.valid())
  i += 6