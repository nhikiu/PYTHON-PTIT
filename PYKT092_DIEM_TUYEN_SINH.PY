class Student:
  def __init__(self, id, name, point, ethnic, area):
    self.id = 'TS{:02d}'.format(id)
    tmp = name.split()
    name = ''
    for i in tmp:
      name += i[0].upper() + i[1:].lower() + ' '
    self.name = name.strip()
    self.point = point
    self.ethnic = ethnic
    self.area = area
  def getTotal(self):
    bonus = 0
    if self.area == '1': bonus += 1.5
    elif self.area == '2': bonus += 1
    if self.ethnic != 'Kinh': bonus += 1.5
    return bonus + self.point
  def getStatus(self):
    if self.getTotal() >= 20.5: return 'Do'
    return 'Truot'
  def __str__(self):
    return f"{self.id} {self.name} {self.getTotal()} {self.getStatus()}"

students = []
for case in range(int(input())):
  students.append(Student(case + 1, input(), float(input()), input(), input()))
students = sorted(students, key=lambda e: (-e.getTotal(), e.id))
print(*students, sep = '\n')