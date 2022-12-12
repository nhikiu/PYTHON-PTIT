n = int(input())
a = []
while len(a) < n:
  a += [int(i) for i in input().split()]
for i in range(n - 1):
  for j in range(i + 1, n):
    if a[i] % 2 == 0 and a[j] % 2 == 0 and a[i] > a[j]:
      a[i], a[j] = a[j], a[i]
    elif a[i] % 2 == 1 and a[j] % 2 == 1 and a[i] < a[j]:
      a[i], a[j] = a[j], a[i]
print(*a)