for case in range(int(input())):
  a, b = input().split()
  fibo = [0,1]
  f0, f1 = 0, 1
  for i in range(2, 93):
    fn = f0 + f1
    fibo += [fn]
    f0, f1 = f1, fn
  for i in range(int(a), int(b) + 1):
    print(fibo[i], end = ' ')
  print()