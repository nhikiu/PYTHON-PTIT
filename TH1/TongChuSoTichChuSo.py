for case in range(int(input())):
  n = input()
  sum = 0
  for i in range(0, len(n), 2):
    sum += int(n[i])
  mul = 1
  le = ''
  for i in range(1,len(n), 2):
    le += str(n[i])
  if int(le) == 0: mul = 0
  else:
    for i in le:
      if i != '0':
        mul *= int(i)
  print(sum, mul, sep = ' ')