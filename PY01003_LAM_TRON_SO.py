for case in range(int(input())):
  n = ' '.join(input()).split()
  for i in range(len(n) - 1, 0, -1):
    if n[i] >= '5':
      n[i - 1] = chr(ord(n[i - 1]) + 1)
    n[i] = '0'
  if n[0] > '9':
    n[0] = '10'
  print(''.join(n))