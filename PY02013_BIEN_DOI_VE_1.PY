while True:
  cnt = 1
  n = int(input())
  if not n: break
  while n != 1:
    if not n % 2: n /= 2
    else: n = n * 3 + 1
    cnt += 1
  print(cnt)