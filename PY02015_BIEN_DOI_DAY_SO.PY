def check(a):
  for i in range(1, len(a)):
    if a[i - 1] != a[i]: return False
  return True

while True:
  inp = [int(i) for i in input().split()]
  if inp == [0] * 4:
    break
  cnt = 0
  while not check(inp):
    a = [0] * 4
    a[0] = abs(inp[0] - inp[1])
    a[1] = abs(inp[1] - inp[2])
    a[2] = abs(inp[2] - inp[3])
    a[3] = abs(inp[3] - inp[0])
    inp = a
    cnt += 1
  print(cnt)