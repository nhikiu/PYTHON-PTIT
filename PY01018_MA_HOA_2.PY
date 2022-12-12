ALPHALBET = ' '.join("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.").split()

while True:
  inp = input()
  if inp[0] == '0': break
  k, s = inp.split()
  k = int(k)
  res = ''
  for i in s:
    res += ALPHALBET[(ALPHALBET.index(i) + k) % 28]
  print(res[::-1])