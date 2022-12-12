import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0: return False
  return True

n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
  if i not in b:
    b += [i]
left = 0
right = sum(i for i in b)
check = False
for i in range(len(b) - 1):
  left += b[i]
  right -= b[i]
  if isPrime(left) and isPrime(right):
    res = i
    check = True
    break
print('NOT FOUND' if not check else res)