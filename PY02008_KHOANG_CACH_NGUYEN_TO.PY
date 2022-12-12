import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i: return False
  return True

prime = []
for i in range(2, 10000):
  if isPrime(i):
    prime += [i]

n, x = [int(i) for i in input().split()]
for i in range(0, n + 1):
  print(x, end = ' ')
  x = x + prime[i]