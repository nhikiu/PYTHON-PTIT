for case in range(int(input())):
  n = input()
  res = 0
  for i in n:
    tmp = 1
    for j in range(1, int(i) + 1):
      tmp *= j
    res += tmp
  print('Yes' if int(n) == res else 'No')