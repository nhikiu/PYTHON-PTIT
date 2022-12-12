for case in range(int(input())):
  n, check = input(), True
  for i in range(2, len(n)):
    if n[i - 2] != n[i]:
      check = False
      break
  print('YES' if check else 'NO')