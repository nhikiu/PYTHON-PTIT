import math

def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return False
  return True

def solve(s):
  cnt = 0
  for i in s:
    if isPrime(int(i)):
      cnt += 1
  return True if cnt > len(s) / 2 else False

for case in range(int(input())):
  s = input()
  print('YES' if len(s) >= 3 and isPrime(len(s)) and solve(s) else 'NO')