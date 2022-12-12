for case in range(int(input())):
  res = '1'
  i = 2
  n = int(input())
  while n >= i:
    cnt = 0
    while n % i == 0:
      cnt += 1
      n /= i
    if cnt > 0:
      res += f" * {i}^{cnt}"
    i += 1
  print(res)