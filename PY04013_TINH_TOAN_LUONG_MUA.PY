import datetime

class Data:
  def __init__(self, id, name, begin, end, quantity):
    self.id = 'T{:02d}'.format(id)
    self.name = name
    self.time = datetime.datetime.strptime(end, '%H:%M') - datetime.datetime.strptime(begin, '%H:%M')
    self.quantity = quantity
  def __str__(self):
    return f"{self.id} {self.name} {'{:.2f}'.format(self.quantity * 3600 / self.time.seconds)}"

list_data = []

def check(data):
  for i in list_data:
    if i.name == data.name:
      i.quantity += data.quantity
      i.time += data.time
      return
  list_data.append(data)

for i in range(int(input())):
  data = Data(len(list_data) + 1, input(), input(), input(), int(input()))
  check(data)
print(*list_data, sep = '\n')