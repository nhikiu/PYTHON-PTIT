import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i: return False
  return True
n = int(input())
l = [int(i) for i in input().split()]
res = {}
for i in l:
  if isPrime(i):
    if i not in res:
      res[i] = 0
    res[i] += 1
for key, value in res.items():
  print(key, value)
