cnt = 0
mark = [0] * 42
while True:
  res = [int(i) for i in input().split()]
  cnt += len(res)
  for i in res:
    mark[i % 42] = 1
  if cnt >= 10: break

ans = 0
for i in mark:
  if i: ans += 1
print(ans)