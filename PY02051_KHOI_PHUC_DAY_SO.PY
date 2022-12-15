n = int(input())
matrix = []
for i in range(n):
  matrix.append([int(i) for i in input().split()])
sum = 0
for i in range(n - 1):
  for j in range(i + 1, n):
    sum += matrix[i][j]
sum //= (n - 1)
res = []
if n > 2:
  for i in range(n):
    tmp = 0
    for j in range(n):
      tmp += matrix[i][j]
    res += [(tmp - sum) // (n - 2)]
elif n == 2:
  res += [sum // 2, sum // 2]
print(*res)