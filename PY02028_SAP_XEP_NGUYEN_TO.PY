import math
#PY02028
def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0: return False
  return True

n = int(input())
a = []
while len(a) < n:
  a += [int(i) for i in input().split()]
for i in range(n - 1):
  for j in range(i + 1, n):
    if isPrime(a[i]) and isPrime(a[j]) and a[i] > a[j]:
      a[i], a[j] = a[j], a[i]
print(*a)