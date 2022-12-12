n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
map = {}
for i in a:
  if i not in map:
    map[i] = 1
  else:
    map[i] += 1
m = max(map.values())
m2 = 0
for i in map.items():
  if i[1] > m2 and i[1] < m:
    m2 = i[1]
res = []
for i in map.items():
  if m2 == i[1]:
    res += [i[0]]
print('NONE' if len(res) == 0 else res[0])