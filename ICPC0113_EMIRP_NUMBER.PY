import math


def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i: return False
  return True

for case in range(int(input())):
  n = int(input())
  res = []
  for i in range(2, n):
    if str(i) != str(i)[::-1] and isPrime(i) and isPrime(int(str(i)[::-1])) and int(str(i)[::-1]) < n:
      if i not in res and int(str(i)[::-1]) not in res:
        res += [i, int(str(i)[::-1])]
  print(*res)