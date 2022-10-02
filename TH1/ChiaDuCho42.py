mark = [0] * 42
check = 0
while True:
  list = [int(i) for i in input().split()]
  check += len(list)
  for i in list:
    mark[i % 42] = 1
  if check == 10:
    break
cnt = 0
for i in mark:
  if i > 0: cnt += 1
print(cnt)