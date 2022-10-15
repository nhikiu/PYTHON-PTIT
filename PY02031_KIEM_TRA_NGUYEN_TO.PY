import math

def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return False
  return True

n, m = [int(i) for i in input().split()]
for r in range(n):
  l = [int(i) for i in input().split()]
  for i in l:
    if isPrime(i):
      print(1, end = ' ')
    else: print(0, end = ' ')
  print()