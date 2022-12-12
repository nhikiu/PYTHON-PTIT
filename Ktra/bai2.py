def checkGiam(n):
  for i in range(1, len(n)):
    if n[i] > n[i - 1]:
      return False
  return True
for case in range(int(input())):
  n = input()
  ch = 'NO'
  if len(n) == 8:
    for i in range(len(n)):
      tmp = n[i:]
      if checkGiam(n[0:i]) and checkGiam(tmp[::-1]):
        ch = 'YES'
        break
  print(ch)
