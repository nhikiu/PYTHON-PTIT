from datetime import datetime

class Athlete:
  def __init__(self, ten, donVi, denDich):
    self.ten = ten
    self.donVi = donVi
    tmp = donVi + " " + ten
    tmp = tmp.split()
    id = ''
    for i in tmp:
      id += i[0]
    self.id = id.upper()
    time = datetime.strptime(denDich, '%H:%M') - datetime.strptime('6:00', '%H:%M')
    self.vanToc = 120 / time.seconds * 3600
  def __str__(self):
    return f"{self.id} {self.ten} {self.donVi} {round(self.vanToc)} Km/h"

athletes = []
for case in range(int(input())):
  athletes.append(Athlete(input(), input(), input()))
athletes = sorted(athletes, key=lambda e: (-e.vanToc))
print(*athletes, sep = '\n')