n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
k = int(input())
top, bottom = 0, 0
for i in range(n):
  for j in range(n):
    if j > n - i - 1:
      bottom += matrix[i][j]
    elif j < n - i - 1:
      top += matrix[i][j]
balance = abs(top - bottom)
print('YES' if balance <= k else 'NO', balance, sep = '\n')