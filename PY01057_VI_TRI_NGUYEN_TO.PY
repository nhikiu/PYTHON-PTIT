import math

PRIME = '2357'

def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return False
  return True

def solve(list):
  for i in range(len(list)):
    if isPrime(i) and not list[i] in PRIME or not isPrime(i) and list[i] in PRIME:
      return False
  return True

for case in range(int(input())):
  list = ' '.join(input()).split()
  print('YES' if solve(list) else 'NO')