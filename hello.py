# PY02008
import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return False
  return True

def check():
  cnt = 1000
  i = 2
  res = []
  while(cnt > 0):
    if isPrime(i):
      cnt -= 1
      res += [i]
    i += 1
  return res

n, x = [int(i) for i in input().split()]
res = check()
list = [x]
for i in range(0, n):
  list += [list[i] + res[i]]
print(*list)
