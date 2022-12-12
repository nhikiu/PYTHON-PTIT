from math import gcd

class PhanSo:
  def __init__(self, tu, mau):
    self.tu = tu
    self.mau = mau
  def add(self, b):
    return PhanSo(self.tu * b.mau + b.tu * self.mau, self.mau * b.mau)
  def rutGon(self):
    tmp = gcd(self.tu, self.mau)
    return PhanSo(self.tu//tmp, self.mau//tmp)
  def __str__(self):
    return f"{self.tu}/{self.mau}"

l = [int(i) for i in input().split()]
p1 = PhanSo(l[0], l[1])
p2 = PhanSo(l[2], l[3])
print(p1.add(p2).rutGon())