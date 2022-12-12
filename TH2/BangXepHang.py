class Student:
  def __init__(self, name, c, t):
    self.name = name
    self.c = c
    self.t = t
  def __str__(self):
    return f"{self.name} {self.c} {self.t}"

list = []
for case in range(int(input())):
  name = input()
  c, t = [int(i) for i in input().split()]
  st = Student(name, c, t)
  list += [st]
list.sort(key=lambda ele: (-ele.c, ele.t, ele.name))
print(*list, sep='\n')