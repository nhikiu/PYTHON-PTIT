matrix = []
n = int(input())
for i in range(n):
  matrix += [[int(i) for i in input().split()]]

k = int(input())
sum = 0
for i in range(n - 1):
  for j in range(i + 1, n):
    sum += matrix[i][j] - matrix[j][i]
print('YES' if abs(sum) <= k else 'NO', abs(sum), sep = '\n')