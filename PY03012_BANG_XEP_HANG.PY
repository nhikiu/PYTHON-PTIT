class Student:
  def __init__(self, name, correctSubmit, totalSubmit):
    self.name = name
    self.correctSubmit = correctSubmit
    self.totalSubmit = totalSubmit
  def __str__(self):
    return f"{self.name} {self.correctSubmit} {self.totalSubmit}"

students = []
for i in range(int(input())):
  name = input()
  c, t = [int(i) for i in input().split()]
  students.append(Student(name, c, t))
students = sorted(students, key=lambda e: (-e.correctSubmit, e.totalSubmit, e.name))
print(*students, sep = '\n')