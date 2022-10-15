import math

n = int(input())
l = [float(i) for i in input().split()]
m, M = min(l), max(l)
for i in l:
  if i == m or i == M:
    del l[l.index(i)]
print('{:.2f}'.format(sum(l)/len(l)))