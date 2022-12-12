for case in range(int(input())):
  n = input()
  sum = 0
  for i in ' '.join(n).split():
    tmp = 1
    for j in range(1, int(i) + 1):
      tmp *= j
    sum += tmp
  print('Yes' if int(n) == sum else 'No')