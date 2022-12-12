s = input()
n = len(s)
if n % 2 == 1: n -= 1
res, list = [], []
for i in range(0, n, 2):
  list += [s[i:i+2]]
  if s[i:i+2] not in res:
    res += [s[i:i+2]]
for i in res:
  print(i, list.count(i))