for case in range(int(input())):
  n = input()
  i = 1
  while i <= 1000 and int(n) % 7:
    n = str(int(n) + int(n[::-1]))
    i += 1
  print(-1 if int(n) % 7 else n)