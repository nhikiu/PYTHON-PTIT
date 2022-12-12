def solve(s):
  if s <= '0119': return 'Ma Ket'
  if s <= '0218': return 'Bao Binh'
  if s <= '0320': return 'Song Ngu'
  if s <= '0419': return 'Bach Duong'
  if s <= '0520': return 'Kim Nguu'
  if s <= '0620': return 'Song Tu'
  if s <= '0722': return 'Cu Giai'
  if s <= '0822': return 'Su Tu'
  if s <= '0922': return 'Xu Nu'
  if s <= '1022': return 'Thien Binh'
  if s <= '1122': return 'Thien Yet'
  if s <= '1221': return 'Nhan Ma'
  else: return 'Ma Ket'

for case in range(int(input())):
  a, b = input().split()
  res = ''
  if len(b) == 1: res += '0'
  res += b
  if len(a) == 1: res += '0'
  res += a
  print(solve(res))