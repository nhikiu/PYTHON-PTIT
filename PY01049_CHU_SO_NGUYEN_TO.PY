import math

def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return False
  return True

def check(num):
  count = 0
  for i in num:
    if isPrime(int(i)):
      count += 1
  return count

for case in range(int(input())):
  num = ' '.join(input()).split()
  if isPrime(len(num)) and check(num) > len(num) - check(num):
    print('YES')
  else:
    print('NO')