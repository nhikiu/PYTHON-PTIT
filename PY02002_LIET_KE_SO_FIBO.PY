def f():
  fibo = [0, 1]
  for i in range(2, 93):
    fibo += [fibo[i - 1] + fibo[i - 2]]
  return fibo

for case in range(int(input())):
  fibo = f()
  a, b = [int(i) for i in input().split()]
  for i in range(a, b + 1):
    print(fibo[i], end = ' ')
  print()