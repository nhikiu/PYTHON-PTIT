def solve(res):
  if res <= '0119': return 'Ma Ket'
  if res <= '0218': return 'Bao Binh'
  if res <= '0320': return 'Song Ngu'
  if res <= '0419': return 'Bach Duong'
  if res <= '0520': return 'Kim Nguu'
  if res <= '0620': return 'Song Tu'
  if res <= '0722': return 'Cu Giai'
  if res <= '0822': return 'Su Tu'
  if res <= '0922': return 'Xu Nu'
  if res <= '1022': return 'Thien Binh'
  if res <= '1122': return 'Thien Yet'
  if res <= '1221': return 'Nhan Ma'
  return 'Ma Ket'

for case in range(int(input())):
  d, m = input().split()
  res = ''
  if len(m) < 2: res += '0'
  res += m
  if len(d) < 2: res += '0'
  res += d
  print(solve(res))