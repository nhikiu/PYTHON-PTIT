for case in range(int(input())):
  str = input() + '/'
  count, c = 0, str[0]
  for i in str:
    if i == c:
      count += 1
    else:
      print(count, c, sep='', end='')
      count, c = 1, i
  print()