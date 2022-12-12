from math import log

Base = '0123456789ABCDEF'

for case in range(int(input())):
  n = int(log(int(input()), 2))
  s = input()
  while len(s) % n != 0:
    s = '0' + s
  res = ''
  pow = [1]
  for i in range(1, n):
    # ..., 32, 16, 8, 4, 2, 1
    pow = [pow[0] * 2] + pow
  for i in range(0, len(s), n):
    tmp = 0
    # gia tri cua tung phan tu
    for j in range(i, i + n):
      tmp = tmp + int(s[j]) * pow[j - i]
    res += Base[tmp]
  print(res)