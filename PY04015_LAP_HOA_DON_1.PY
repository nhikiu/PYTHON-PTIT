class Customer:
  def __init__(self, id, name, old, new):
    self.id = 'KH{:02d}'.format(id)
    self.name = name
    self.dis = new - old
  def getAmount(self):
    if self.dis <= 50: return self.dis * 100 * 1.02
    if self.dis <= 100: return (50 * 100 + (self.dis - 50) * 150) * 1.03
    return (50 * 100 + 50 * 150 + (self.dis - 100) * 200) * 1.05
  def __str__(self):
    return f"{self.id} {self.name} {round(self.getAmount())}"

customers = []
for case in range(int(input())):
  customers += [Customer(case + 1, input(), int(input()), int(input()))]
customers = sorted(customers, key=lambda e: (-e.getAmount()))
print(*customers, sep='\n')