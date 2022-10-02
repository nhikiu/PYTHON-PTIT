P = ' '.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.').split()

while True:
  s = input()
  if s == '0':
    break
  k, str = s.split()
  res = ''
  for i in str:
    res += P[(P.index(i) + int(k)) % 28]
  print(res[::-1])