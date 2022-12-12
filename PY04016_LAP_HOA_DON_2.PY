from datetime import datetime

class Customer:
  def __init__(self, id, name, room, checkin, checkout, serviceCharge):
    self.id = 'KH{:02d}'.format(id)
    self.name = name
    self.room = room
    time = datetime.strptime(checkout, '%d/%m/%Y') - datetime.strptime(checkin, '%d/%m/%Y')
    self.time = time.days + 1
    self.serviceCharge = serviceCharge
  def getAmount(self):
    unitPrice = 0
    if self.room[0] == '1': unitPrice = 25
    elif self.room[0] == '2': unitPrice = 34
    elif self.room[0] == '3': unitPrice = 50
    elif self.room[0] == '4': unitPrice = 80
    return unitPrice * self.time + self.serviceCharge
  def __str__(self):
    return f"{self.id} {self.name} {self.room} {self.time} {self.getAmount()}"

customers = []
for case in range(int(input())):
  customers.append(Customer(case + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input())))
customers = sorted(customers, key=lambda e: (-e.getAmount()))
print(*customers, sep = '\n')