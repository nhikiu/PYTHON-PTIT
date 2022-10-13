import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return False
  return True

for case in range(int(input())):
  n = int(input())
  res = []
  for i in range(2, int(n) + 1):
    rv_i = str(i)[::-1]
    if isPrime(i) and isPrime(int(rv_i)) and i != int(rv_i) and int(rv_i) <= n and i not in res and rv_i not in res:
      res += [i, int(rv_i)]
      print(i, rv_i, end = ' ')
  print()