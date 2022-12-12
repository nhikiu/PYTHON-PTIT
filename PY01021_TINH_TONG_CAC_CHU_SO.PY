for case in range(int(input())):
  s = input()
  sum = 0
  res = ''
  for i in s:
    if i.isdigit():
      sum += int(i)
    else: res += i
  print(*sorted(res), sum, sep = '')