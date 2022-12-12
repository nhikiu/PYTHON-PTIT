class Teacher:
  def __init__(self, id, name, code, p1, p2):
    self.id = 'GV{:02d}'.format(id)
    self.name = name
    self.code = code
    self.point = p1 * 2 + p2
  def getSubject(self):
    c = self.code[0]
    if c == 'A': return 'TOAN'
    if c == 'B': return 'LY'
    if c == 'C': return 'HOA'
  def getBonusPoint(self):
    p = self.code[1]
    if p == '1': return 2
    if p == '2': return 1.5
    if p == '3': return 1
    return 0
  def getTotalPoint(self):
    return self.point + self.getBonusPoint()
  def getStatus(self):
    if self.getTotalPoint() >= 18: return 'TRUNG TUYEN'
    return 'LOAI'
  def __str__(self):
    return f"{self.id} {self.name} {self.getSubject()} {'{:.1f}'.format(self.getTotalPoint())} {self.getStatus()}"

teachers = []
for case in range(int(input())):
  teachers.append(Teacher(case + 1, input(), input(), float(input()), float(input())))
teachers = sorted(teachers, key=lambda e: (-e.getTotalPoint()))
print(*teachers, sep = '\n')