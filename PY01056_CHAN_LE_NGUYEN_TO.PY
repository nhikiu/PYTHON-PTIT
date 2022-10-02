import math

def check(s):
  for i in range(len(s)):
    if (not i % 2 and int(s[i]) % 2) or (i % 2 and not int(s[i]) % 2):
      return False
  return True

def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return False
  return True

for case in range(int(input())):
  str = input()
  s = sum(int(i) for i in str)
  print('YES' if isPrime(s) and check(str) else 'NO')