def solve(a, b, c):
  if c == 'IN':
    if a == 'Xe_con':
      if b == '5': return 10000
      elif b == '7': return 15000
    elif a == 'Xe_tai' and b == '2': return 20000
    elif a == 'Xe_khach':
      if b == '29': return 50000
      elif b == '45': return 70000
  return 0

res = {}
for case in range(int(input())):
  inp = input().split()
  fee = solve(inp[1], inp[2], inp[3])
  if inp[4] not in res.keys():
    res[inp[4]] = fee
  else:
    res[inp[4]] = res[inp[4]] + fee
for i in res.items():
  print(f'{i[0]}: {i[1]}')