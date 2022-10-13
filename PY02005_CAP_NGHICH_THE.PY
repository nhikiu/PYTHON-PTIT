n = int(input())
cnt = 0
list = [int(i) for i in input().split()]
for i in range(n):
  for j in range(i + 1, n):
    if list[i] > list[j]:
      cnt += 1
print(cnt)