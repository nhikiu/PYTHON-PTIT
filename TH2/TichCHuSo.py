for case in range(int(input())):
  num = ' '.join(input()).split()
  res = 1
  for i in num:
    if i != '0':
      res *= int(i)
  print(res)