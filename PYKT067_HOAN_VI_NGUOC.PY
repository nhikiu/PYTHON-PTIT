import itertools

for case in range(int(input())):
  n = int(input())
  a = list(itertools.permutations(range(1, n + 1)))
  a = sorted(a, reverse=True)
  print(len(a))
  for i in a:
    print(*i, sep = '', end = ' ')
  print()