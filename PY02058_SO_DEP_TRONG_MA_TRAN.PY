import math

r, c = [int(i) for i in input().split()]
matrix = []
for i in range(r):
  matrix.append([int(i) for i in input().split()])
max, min = matrix[0][0], matrix[0][0]
for i in range(r):
  for j in range(c):
    if matrix[i][j] > max:
      max = matrix[i][j]
    if matrix[i][j] < min:
      min = matrix[i][j]
dis = max - min
check = False
for i in range(r):
  for j in range(c):
    if matrix[i][j] == dis:
      check = True
      break
if not check: print('NOT FOUND')
else:
  print(dis)
  for i in range(r):
    for j in range(c):
      if dis == matrix[i][j]:
        print(f'Vi tri [{i}][{j}]')