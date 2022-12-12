import math


def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i: return False
  return True

for case in range(int(input())):
  n = int(input())
  cnt = 0
  for i in range(2, n - 5):
    if isPrime(i) and isPrime(i + 6) and (isPrime(i + 2) or isPrime(i + 4)):
      cnt += 1
  print(cnt)