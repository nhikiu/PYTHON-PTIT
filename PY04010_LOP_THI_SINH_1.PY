class Candidate:
  def __init__(self, name, dob, p1, p2, p3):
    self.name = name
    self.dob = dob
    self.p = p1 + p2 + p3
  def __str__(self):
    return f"{self.name} {self.dob} {'{:.1f}'.format(self.p)}"

print(Candidate(input(), input(), float(input()), float(input()), float(input())))