from math import gcd

class PhanSo:
  def __init__(self, tu, mau):
    self.tu = tu
    self.mau = mau
  def rutGon(self):
    tmp = gcd(self.tu, self.mau)
    return PhanSo(self.tu//tmp, self.mau//tmp)
  def __str__(self):
    return f"{self.tu}/{self.mau}"

tu, mau = [int(i) for i in input().split()]
p = PhanSo(tu, mau)
print(p.rutGon())