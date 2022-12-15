n = int(input())
list = []
for i in range(n):
  list += [input()]
res = []
for i in list:
  sum = 0
  for j in list:
    if j != i:
      tmp = j + j[0 : len(j) - 1]
      if tmp.find(i) == -1:
        res = [-1]
        break
      sum += tmp.find(i)
  res += [sum]
print(min(res))