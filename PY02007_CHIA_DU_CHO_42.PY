list = []
mark = [0] * 42
while len(list) < 10:
  list += [int(i) for i in input().split()]

for i in list:
  mark[i % 42] = 1
cnt = 0
for i in mark:
  if i == 1:
    cnt += 1
print(cnt)