class Student:
  def __init__(self, id, name, listPoint):
    self.id = 'HS{:02d}'.format(id)
    self.name = name
    listPoint = [float(i) for i in listPoint.split()]
    self.point = (sum(listPoint) + listPoint[0] + listPoint[1]) / 10 / 1.2

  def xl(self):
    if self.point >= 9: return 'XUAT SAC'
    if self.point >= 8: return 'GIOI'
    if self.point >= 7: return 'KHA'
    if self.point >= 5: return 'TB'
    return 'YEU'

  def __str__(self):
    return f"{self.id} {self.name} {'{:.1f}'.format(self.point)} {self.xl()}"


students = []
for case in range(int(input())):
  students += [Student(case + 1, input(), input())]
students = sorted(students, key=lambda e: (-e.point, e.id))
for i in students:
  print(i)