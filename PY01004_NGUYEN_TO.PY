import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i: return False
  return True

for case in range(int(input())):
  n, cnt = int(input()), 1
  for i in range(2, n):
    if math.gcd(i, n) == 1:
      cnt += 1
  print('YES' if isPrime(cnt) else 'NO')