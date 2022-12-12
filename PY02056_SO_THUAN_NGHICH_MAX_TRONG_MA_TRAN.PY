import math

def thuanNghich(n):
  if len(str(n)) >= 2 and n == int(str(n)[::-1]): return True
  return False

r, c = [int(i) for i in input().split()]
matrix = []
for i in range(r):
  matrix.append([int(i) for i in input().split()])
max = 0
for i in range(r):
  for j in range(c):
    if thuanNghich(matrix[i][j]) and matrix[i][j] > max:
      max = matrix[i][j]
if max == 0: print('NOT FOUND')
else:
  print(max)
  for i in range(r):
    for j in range(c):
      if max == matrix[i][j]:
        print(f'Vi tri [{i}][{j}]')