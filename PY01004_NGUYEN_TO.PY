import math

def isPrime(n):
  if n < 2:
    return False
  sq = int(math.sqrt(n)) + 1
  for i in range(2,sq):
    if not n%i:
      return False
  return True

for case in range(int(input())):
  n = int(input())
  count = 0
  for i in range(1, n):
    if math.gcd(i,n) == 1:
      count += 1

  if isPrime(count):
    print('YES')
  else:
    print('NO')