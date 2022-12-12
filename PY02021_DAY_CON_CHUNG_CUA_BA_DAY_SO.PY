for case in range(int(input())):
  n, m, k =[int(i) for i in input().split()]
  a = [int(i) for i in input().split()]
  b = [int(i) for i in input().split()]
  c = [int(i) for i in input().split()]
  i1, i2, i3 = 0, 0, 0
  res = []
  while (i1 < n and i2 < m and i3 < k):
    if a[i1] == b[i2] and b[i2] == c[i3]:
      res.append(a[i1])
      i1 += 1
      i2 += 1
      i3 += 1
    elif a[i1] < b[i2]: i1 += 1
    elif b[i2] < c[i3]: i2 += 1
    elif c[i3] < a[i1]: i3 += 1
  if len(res) == 0: print('NO')
  else: print(*res)