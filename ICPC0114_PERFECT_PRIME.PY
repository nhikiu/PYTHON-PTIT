import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return False
  return True

def checkPrime(n):
  for i in n:
    if not isPrime(int(i)):
      return False
  return True

for case in range(int(input())):
  n = input()
  if isPrime(int(n)) and isPrime(int(n[::-1])) and isPrime(sum(int(i) for i in ' '.join(n).split())) and checkPrime(n):
    print('Yes')
  else: print('No')