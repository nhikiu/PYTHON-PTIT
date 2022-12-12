class Team:
  def __init__(self, id, name, school):
    self.id = 'Team{:02d}'.format(id)
    self.name = name
    self.school = school
class Candidate:
  def __init__(self, id, name, team):
    self.id = 'C{:03d}'.format(id)
    self.name = name
    self.team = team
  def __str__(self):
    return f"{self.id} {self.name} {self.team.name} {self.team.school}"

teams = []
for i in range(int(input())):
  teams.append(Team(i + 1, input(), input()))
candidates = []
for i in range(int(input())):
  name = input()
  id_team = input()
  for j in teams:
    if id_team == j.id:
      team = j
  candidates.append(Candidate(i + 1, name, team))
candidates = sorted(candidates, key=lambda e: (e.name))
print(*candidates, sep = '\n')