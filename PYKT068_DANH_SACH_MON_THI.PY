class MonThi:
  def __init__(self, ma, ten, hinhThucThi):
    self.ma = ma
    self.ten = ten
    self.hinhThucThi = hinhThucThi
  def __str__(self):
    return f"{self.ma} {self.ten} {self.hinhThucThi}"

list = []
for case in range(int(input())):
  list.append(MonThi(input(), input(), input()))
list = sorted(list, key=lambda e: (e.ma))
print(*list, sep = '\n')