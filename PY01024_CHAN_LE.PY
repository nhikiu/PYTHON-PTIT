import math

def checkA(n):
  if not sum(int(i) for i in n) % 10:
    return True
  return False

def checkB(n):
  for i in range(0, len(n) - 1):
    if math.fabs(ord(n[i]) - ord(n[i + 1])) != 2:
      return False
  return True


for case in range(int(input())):
  n = ' '.join(input()).split()
  if checkA(n) and checkB(n):
    print('YES')
  else:
    print('NO')