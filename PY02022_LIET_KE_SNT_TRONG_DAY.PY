import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i: return False
  return True

n = int(input())
a = [int(i) for i in input().split()]
res = {}
for i in a:
  if isPrime(i):
    if i not in res:
      res[i] = 0
    res[i] += 1
for k, v in res.items():
  print(k, v)