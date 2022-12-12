import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i: return False
  return True

for case in range(int(input())):
  a, b = [int(i) for i in input().split()]
  print('YES' if isPrime(sum(int(i) for i in ' '.join(str(math.gcd(a, b))).split())) else 'NO')