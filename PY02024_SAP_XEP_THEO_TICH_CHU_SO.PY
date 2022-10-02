def mul(n):
  s = 1
  for i in n:
    s *= int(i)
  return s

for case in range(int(input())):
  n = int(input())
  print(*sorted([i for i in input().split()], key=lambda ele: (mul(ele), int(ele))))