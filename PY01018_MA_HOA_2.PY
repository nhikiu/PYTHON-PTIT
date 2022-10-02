list = ' '.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.').split()

while True:
  inp = input()
  if inp == '0':
    break
  k, str = inp.split()
  k = int(k)
  res = ''
  for i in str:
    res += list[(list.index(i) + k) % 28]
  print(res[::-1])