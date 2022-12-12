for case in range(int(input())):
  n = int(input())
  cnt = 0
  while True:
    if n % 7 == 0 or cnt == 1000:
      break
    n = n + int(str(n)[::-1])
    cnt += 1
  print(n if cnt < 1000 else -1)