import math

n, k = [int(i) for i in input().split()]
s, cnt = int(math.pow(10,k)), 0
for i in range(s//10, s):
  if math.gcd(i, n) == 1:
    cnt += 1
    print(i, end = ' ')
    if not cnt % 10: print()