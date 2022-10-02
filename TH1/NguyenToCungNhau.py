import math

n, k = input().split()
s = int(math.pow(10,int(k)))
cnt = 0
for i in range(s//10, s):
  if math.gcd(int(n), i) == 1:
    cnt += 1
    print(i, end = ' ')
    if not cnt % 10:
      print()