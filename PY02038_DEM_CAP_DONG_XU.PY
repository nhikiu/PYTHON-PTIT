n = int(input())
a = []
for i in range(n):
  a.append(' '.join(input()).split())
cnt = 0
for i in range(n):
  for j in range(n - 1):
    for k in range(j + 1, n):
      if a[i][j] == a[i][k] == 'C':
        cnt += 1
      if a[j][i] == a[k][i] == 'C':
        cnt += 1
print(cnt)