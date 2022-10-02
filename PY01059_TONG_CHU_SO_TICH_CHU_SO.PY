for case in range(int(input())):
  n = input()
  s, mul, res = 0, 1, ''
  for i in range(0, len(n), 2):
    s += int(n[i])
  for i in range(1, len(n), 2):
    res += n[i]
  if int(res) == 0: mul = 0
  else:
    for i in res:
      if i != '0':
        mul *= int(i)
  print(s, mul)