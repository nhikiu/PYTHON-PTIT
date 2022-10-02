import math

n = input()
list = [int(i) for i in input().split()]
list = sorted(list)
for i in range(len(list) - 1):
  for j in range(i + 1, len(list)):
    if math.gcd(list[i], list[j]) == 1:
      print(list[i], list[j])