import math


def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n) + 1)):
    if not n % i:
      return False
  return True


for case in range(int(input())):
  str = input()
  num = int(str[len(str) - 4: len(str)])
  print('YES' if isPrime(num) else 'NO')