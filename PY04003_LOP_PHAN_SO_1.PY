from math import gcd

class PhanSo:
  def __init__(self, tu, mau):
    self.__tu = tu
    self.__mau = mau
  def solve(self):
    tmp = gcd(self.__tu, self.__mau)
    return f"{self.__tu//tmp}/{self.__mau//tmp}"

inp = [int(i) for i in input().split()]
p = PhanSo(inp[0], inp[1])
print(p.solve())