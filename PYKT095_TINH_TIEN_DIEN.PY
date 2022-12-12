class HoGiaDinh:
  def __init__(self, id, ten, loai, chiSoDau, chiSoCuoi):
    self.id = 'KH{:02d}'.format(id)
    self.ten = self.getName(ten)
    self.loai = loai
    self.chiSo = chiSoCuoi - chiSoDau
  def getName(self, ten):
    tmp = ten.split()
    res = ''
    for i in tmp:
      res += i[0].upper() + i[1:].lower() + ' '
    return res.strip()
  def dinhMuc(self):
    if self.loai == 'A': return 100
    if self.loai == 'B': return 500
    if self.loai == 'C': return 200
  def trongDinhMuc(self):
    if self.chiSo < self.dinhMuc(): return self.chiSo * 450
    return self.dinhMuc() * 450
  def vuotDinhMuc(self):
    if self.chiSo > self.dinhMuc(): return (self.chiSo - self.dinhMuc()) * 1000
    return 0
  def vat(self):
    return self.vuotDinhMuc() // 20
  def tongTien(self):
    return self.trongDinhMuc() + self.vuotDinhMuc() + self.vat()
  def __str__(self):
    return f"{self.id} {self.ten} {self.trongDinhMuc()} {self.vuotDinhMuc()} {self.vat()} {self.tongTien()}"

list = []
for case in range(int(input())):
  name = input()
  loai, chiSoDau, chiSoCuoi = input().split()
  list.append(HoGiaDinh(case + 1, name, loai, int(chiSoDau), int(chiSoCuoi)))
list = sorted(list, key=lambda e: (-e.tongTien()))
print(*list, sep = '\n')