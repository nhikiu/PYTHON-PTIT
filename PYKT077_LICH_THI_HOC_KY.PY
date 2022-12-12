from datetime import datetime

class Subject:
  def __init__(self, id, name):
    self.id = id
    self.name = name

class Shift:
  def __init__(self, id, subject, date, time, className):
    self.id = 'T{:03d}'.format(id)
    self.subject = subject
    self.date = date
    self.time = time
    self.className = className
  def __str__(self):
    return f"{self.id} {self.subject.id} {self.subject.name} {self.date} {self.time} {self.className}"

n, m = [int(i) for i in input().split()]
subjects = []
for i in range(n):
  subjects.append(Subject(input(), input()))
shifts = []
for i in range(m):
  inp = input().split()
  for j in subjects:
    if inp[0] == j.id:
      inp[0] = j
  shifts.append(Shift(i + 1, inp[0], inp[1], inp[2], inp[3]))
shifts = sorted(shifts, key=lambda e: (datetime.strptime(e.date, '%d/%m/%Y'), e.time, e.subject.id))
print(*shifts, sep = '\n')