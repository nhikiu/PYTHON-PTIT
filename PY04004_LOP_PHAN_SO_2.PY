from math import gcd

class PhanSo:
  def __init__(self, tu, mau):
    self.__tu = tu
    self.__mau = mau
  def add(self, p):
    return PhanSo(self.__tu * p.__mau + p.__tu * self.__mau, self.__mau * p.__mau)
  def solve(self):
    tmp = gcd(self.__tu, self.__mau)
    return f"{self.__tu//tmp}/{self.__mau//tmp}"

inp = [int(i) for i in input().split()]
p1 = PhanSo(inp[0], inp[1])
p2 = PhanSo(inp[2], inp[3])
print(p1.add(p2).solve())