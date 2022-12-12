class Department:
  def __init__(self, id, name):
    self.id = id
    self.name = name

class Employee:
  def __init__(self, id, department, name, basicSalary, workingDay):
    self.id = id
    self.department = department
    self.name = name
    self.basicSalary = basicSalary
    self.workingDay = workingDay
  def getSalaryScale(self):
    group = self.id[0]
    exp = int(self.id[1:3])
    if group == 'A':
      if exp <= 3: return 10
      if exp <= 8: return 12
      if exp <= 15: return 14
      return 20
    if group == 'B':
      if exp <= 3: return 10
      if exp <= 8: return 11
      if exp <= 15: return 13
      return 16
    if group == 'C':
      if exp <= 3: return 9
      if exp <= 8: return 10
      if exp <= 15: return 12
      return 14
    if group == 'D':
      if exp <= 3: return 8
      if exp <= 8: return 9
      if exp <= 15: return 11
      return 13

  def getSalary(self):
    return self.basicSalary * self.workingDay * self.getSalaryScale() * 1000;
  def __str__(self):
    return f"{self.id} {self.name} {self.department.name} {self.getSalary()}"

departments = []
for i in range(int(input())):
  s = input()
  departments.append(Department(s[0:2], s[3:]))
employees = []
for i in range(int(input())):
  id = input()
  for j in departments:
    if id[-2:] == j.id:
      department = j
  employees.append(Employee(id, department, input(), int(input()), int(input())))
print(*employees, sep = '\n')