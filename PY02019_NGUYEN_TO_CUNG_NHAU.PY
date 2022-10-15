from math import gcd

n = int(input())
l = [int(i) for i in input().split()]
l.sort()
for i in range(0, len(l) - 1):
  for j in range(i + 1, len(l)):
    if gcd(l[i], l[j]) == 1:
      print(l[i], l[j])