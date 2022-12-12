for case in range(int(input())):
  num = ' '.join(input()).split()
  num.sort()
  sum = 0
  for i in num:
    if i >= '0' and i <= '9':
      sum += int(i)
  for i in num:
    if i < '0' or i > '9':
      print(i, end='')
  print(sum)