class Customer:
  def __init__(self, id, name, checkin, checkout):
    self.id = id
    self.name = name
    self.checkin = checkin
    self.checkout = checkout
  def getTime(self):
    h = int(self.checkout[0:2]) - int(self.checkin[0:2])
    m = int(self.checkout[3:5]) - int(self.checkin[3:5])
    if m < 0:
      m += 60
      h -= 1
    return f"{'{:02d}'.format(h)}{'{:02d}'.format(m)}"
  def __str__(self):
    return f"{self.id} {self.name} {int(self.getTime()[0:2])} gio {int(self.getTime()[2:4])} phut"

customers = []
for case in range(int(input())):
  customers += [Customer(input(), input(), input(), input())]
customers = sorted(customers, key=lambda e: (e.getTime()), reverse=True)
print(*customers, sep = '\n')