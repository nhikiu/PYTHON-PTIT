class SoPhuc:
  def __init__(self, thuc, ao):
    self.thuc = thuc
    self.ao = ao
  def __str__(self):
    if self.ao < 0:
      return f"{self.thuc} - {-self.ao}i"
    return f"{self.thuc} + {self.ao}i"
  def add(self, b):
    return SoPhuc(self.thuc + b.thuc, self.ao + b.ao)
  def mul(self, b):
    thuc = self.thuc * b.thuc - self.ao * b.ao
    ao = self.ao * b.thuc + self.thuc * b.ao
    return SoPhuc(thuc, ao)

for case in range(int(input())):
  inp = [int(i) for i in input().split()]
  a = SoPhuc(inp[0], inp[1])
  b = SoPhuc(inp[2], inp[3])
  print(a.add(b).mul(a), a.add(b).mul(a.add(b)), sep = ', ')