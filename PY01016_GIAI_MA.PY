for case in range(int(input())):
  a = input()
  for i in range(1, len(a), 2):
    print(a[i - 1] * int(a[i]), end = '')
  print()