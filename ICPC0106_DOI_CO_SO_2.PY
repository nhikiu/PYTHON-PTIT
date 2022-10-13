import math

BASE = '0123456789ABCDEF'

for case in range(int(input())):
  ind = int(math.log2(int(input())))
  n = input()
  res = ''
  while len(n) % ind:
    n = '0' + n
  pow = [1]
  for i in range(1, ind):
    pow = [pow[0] * 2] + pow
  for i in range(0, len(n), ind):
    tmp = 0
    for j in range(i, i + ind):
      tmp = tmp + int(n[j]) * pow[j - i]
    res += BASE[tmp]
  print(res)