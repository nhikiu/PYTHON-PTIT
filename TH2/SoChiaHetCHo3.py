for case in range(int(input())):
  num = ' '.join(input()).split()
  s = sum(int(i) for i in num)
  print('YES' if not s % 3 else 'NO')