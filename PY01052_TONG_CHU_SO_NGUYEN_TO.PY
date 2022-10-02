import math

def isPrime(n):
  if n < 2:
    return 'NO'
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      return 'NO'
  return 'YES'

for case in range(int(input())):
  s = sum(int(i) for i in input())
  print(isPrime(s))