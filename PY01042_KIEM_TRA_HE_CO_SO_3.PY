def check(s):
  for i in s:
    if i != '0' and i != '1' and i != '2':
      return False
  return True

for case in range(int(input())):
  print('YES' if check(input()) else 'NO')