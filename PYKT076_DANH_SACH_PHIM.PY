from datetime import datetime
# PYKT076

class Category:
  def __init__(self, id, name):
    self.id = 'TL{:03d}'.format(id)
    self.name = name

class Cinema:
  def __init__(self, id, category, date, name, episode):
    self.id = 'P{:03d}'.format(id)
    self.category = category
    self.date = date
    self.name = name
    self.episode = episode
  def __str__(self):
    return f"{self.id} {self.category.name} {self.date} {self.name} {self.episode}"
categories = []
n, m = [int(i) for i in input().split()]
for i in range(n):
  categories.append(Category(i + 1, input()))
cinemas = []
for i in range(m):
  id_category = input()
  for j in categories:
    if id_category == j.id:
      category = j
  cinemas.append(Cinema(i + 1, category, input(), input(), input()))
cinemas = sorted(cinemas, key=lambda e: (datetime.strptime(e.date, '%d/%m/%Y'), e.name, -int(e.episode)))
print(*cinemas, sep = '\n')