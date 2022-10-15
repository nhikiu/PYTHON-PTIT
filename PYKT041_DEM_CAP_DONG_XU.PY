n = int(input())
matrix = [[i for i in ' '.join(input()).split()] for j in range(n)]
cnt = 0
for i in range(n):
  for j in range(n - 1):
    if matrix[i][j] == 'C':
      for k in range(j + 1, n):
        if matrix[i][k] == 'C':
          cnt += 1
for i in range(n - 1):
  for j in range(n):
    if matrix[i][j] == 'C':
      for k in range(i + 1, n):
        if matrix[k][j] == 'C':
          cnt += 1
print(cnt)