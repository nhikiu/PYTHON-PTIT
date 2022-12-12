class Student:
  def __init__(self, name, dob, f1, f2, f3):
    self.name = name
    self.dob = dob
    self.f1 = f1
    self.f2 = f2
    self.f3 = f3
    self.tb = (f1 + f2 + f3 + min(f1, f2, f3)) / 4
  def __str__(self):
    return f"{self.name} {self.dob} {'{:.1f}'.format(self.tb)}"
res = []
for case in range(int(input())):
  st = Student(input(), input(), float(input()), float(input()), float(input()))
  res += [st]
res = sorted(res, key=lambda ele: (-ele.tb))
for i in res:
  print(i)