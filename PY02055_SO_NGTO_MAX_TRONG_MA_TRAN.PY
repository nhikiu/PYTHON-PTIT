import math

def isPrime(n):
  if n < 2: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

r, c = [int(i) for i in input().split()]
matrix = []
for i in range(r):
  matrix.append([int(i) for i in input().split()])
max = 0
for i in range(r):
  for j in range(c):
    if isPrime(matrix[i][j]) and matrix[i][j] > max:
      max = matrix[i][j]
if max == 0: print('NOT FOUND')
else:
  print(max)
  for i in range(r):
    for j in range(c):
      if max == matrix[i][j]:
        print(f'Vi tri [{i}][{j}]')