from math import ceil


class Student:
  def __init__(self, id, name, p1, p2, p3):
    self.id = 'SV{:02d}'.format(id)
    tmp = name.split()
    name = ''
    for i in tmp:
      name += i[0].upper() + i[1:].lower() + ' '
    self.name = name.strip()
    self.point = (p1 * 3 + p2 * 3 + p3 * 2) / 8
    self.rank = 0
  def __str__(self):
    return f"{self.id} {self.name} {'{:.2f}'.format(ceil(self.point * 100)/100)} {self.rank}"

students = []
for case in range(int(input())):
  students.append(Student(case + 1, input(), int(input()), int(input()), int(input())))
students = sorted(students, key=lambda e: (-e.point))
students[0].rank = 1
for i in range(1, len(students)):
  if students[i].point == students[i - 1].point:
    students[i].rank = students[i - 1].rank
  else:
    students[i].rank = i + 1

students = sorted(students, key=lambda e: (e.rank, e.id))
print(*students, sep = '\n')