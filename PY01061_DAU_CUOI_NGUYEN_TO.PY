import math

def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return False
  return True

for case in range(int(input())):
  s = input()
  print('YES' if len(s) >= 4 and isPrime(int(s[0:3])) and isPrime(int(s[len(s) - 3:])) else 'NO')