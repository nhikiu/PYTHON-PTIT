class Item:
  def __init__(self, id, name, quantity, unitPrice, discount):
    self.id = id
    self.name = name
    self.quantity = quantity
    self.unitPrice = unitPrice
    self.discount = discount
  def getTotal(self):
    return self.unitPrice * self.quantity - self.discount
  def __str__(self):
    return f"{self.id} {self.name} {self.quantity} {self.unitPrice} {self.discount} {self.getTotal()}"

items = []
for case in range(int(input())):
  items.append(Item(input(), input(), int(input()), int(input()), int(input())))
items = sorted(items, key=lambda e: (-e.getTotal()))
print(*items, sep = '\n')