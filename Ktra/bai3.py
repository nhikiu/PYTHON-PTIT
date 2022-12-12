class NhanVien:
  def __init__(self, ma, ten, vao, ra):
    self.ma = ma
    self.ten = ten
    self.vao = vao
    self.ra = ra
  def tinhGio(self):
    gio = int(self.ra[0:2]) - int(self.vao[0:2])
    phut = int(self.ra[3:5]) - int(self.vao[3:5])
    if phut < 0:
      phut += 60
      gio -= 1
    res = []
    res += [gio - 1]
    res += [phut]
    return res
  def __str__(self):
    if self.tinhGio()[0] < 8:
      return f"{self.ma} {self.ten} {self.tinhGio()[0]} gio {self.tinhGio()[1]} phut THIEU"
    return f"{self.ma} {self.ten} {self.tinhGio()[0]} gio {self.tinhGio()[1]} phut DU"
res = []
for case in range(int(input())):
  nv = NhanVien(input(), input(), input(), input())
  res += [nv]
res.sort(key= lambda ele: (ele.tinhGio()))
for i in range(len(res) - 1, -1, -1):
  print(res[i])