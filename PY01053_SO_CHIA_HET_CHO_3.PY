for case in range(int(input())):
  s = sum(int(i) for i in ' '.join(input()).split())
  print('NO' if s % 3 else 'YES')