class Candidate:
  def __init__(self, id, name, p1, p2):
    self.id = f"TS0{id}"
    self.name = name
    if p1 > 10: p1 /= 10
    self.p1 = p1
    if p2 > 10: p2 /= 10
    self.p2 = p2
  def getPoint(self):
    return (self.p1 + self.p2) / 2
  def getStatus(self):
    p = self.getPoint()
    if p < 5: return 'TRUOT'
    if p < 8: return 'CAN NHAC'
    if p <= 9.5: return 'DAT'
    return 'XUAT SAC'
  def __str__(self):
    return f"{self.id} {self.name} {'{:.2f}'.format(self.getPoint())} {self.getStatus()}"

candidates = []
for case in range(int(input())):
  candidates += [Candidate(case + 1, input(), float(input()), float(input()))]
candidates = sorted(candidates, key=lambda e: (-e.getPoint()))
print(*candidates, sep = '\n')