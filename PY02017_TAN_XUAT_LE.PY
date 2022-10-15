for case in range(int(input())):
  n = int(input())
  l = [int(i) for i in input().split()]
  res = {}
  for i in l:
    if i not in res:
      res[i] = 0
    res[i] += 1
  for key, value in res.items():
    if value % 2:
      print(key)
      break