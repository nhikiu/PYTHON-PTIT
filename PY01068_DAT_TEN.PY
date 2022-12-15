import itertools

n, k = [int(i) for i in input().split()]
a = sorted({i for i in input().split()})
for i in list(itertools.combinations(a, k)):
  print(*i)