n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
res1, res2, res3 = [], [], []
for i in a:
  if i in b:
    res1 += [i]
for i in a:
  if i not in b:
    res2 += [i]
for i in b:
  if i not in a:
    res3 += [i]
print(*sorted(set(res1)))
print(*sorted(set(res2)))
print(*sorted(set(res3)))