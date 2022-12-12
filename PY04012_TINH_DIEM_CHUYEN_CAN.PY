class Student:
  def __init__(self, id, name, className):
    self.id = id
    self.name = name
    self.className = className
    self.point = 10
  def __str__(self):
    return f"{self.id} {self.name} {self.className} {self.point}"

def check(s):
  p = 10
  for i in s:
    if i == 'm': p -= 1
    elif i == 'v': p -= 2
  return '0 KDDK' if p <= 0 else p

students = []
t = int(input())
for case in range(t):
  students.append(Student(input(), input(), input()))
for case in range(t):
  inp = input().split()
  for i in students:
    if i.id == inp[0]:
      i.point = check(inp[1])
print(*students, sep = '\n')