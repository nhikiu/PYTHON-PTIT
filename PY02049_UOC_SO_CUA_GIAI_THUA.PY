for case in range(int(input())):
  n, p = [int(i) for i in input().split()]
  tmp = 1
  cnt = 0
  for i in range(n, 1, -1):
    tmp = i
    while tmp % p == 0:
      tmp /= p
      cnt += 1
  print(cnt)