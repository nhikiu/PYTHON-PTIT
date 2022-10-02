n = int(input())
a =[[]] * n

for i in range(n):
  a[i] = [int(i) for i in input().split()]
k = int(input())
sum1, sum2 = 0, 0
for i in range(n):
  for j in range(n):
    if i < j:
      sum1 += a[i][j]
    elif j < i:
      sum2 += a[i][j]
res = abs(sum1 - sum2)
print('YES' if res <= k else 'NO', res, sep = '\n')