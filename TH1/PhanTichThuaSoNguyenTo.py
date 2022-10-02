import math

for case in range(int(input())):
  res = '1'
  n = int(input())
  for i in range(2, int(math.sqrt(n)) + 1):
    cnt = 0
    while not n % i:
      cnt += 1
      n /= i
    if cnt != 0:
      res += ' * ' + str(i) + '^' + str(cnt)
  if n > 1:
    res += ' * ' + str(int(n)) + '^1'
  print(res)
