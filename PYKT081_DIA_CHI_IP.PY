def check(s):
  for i in s:
    if not i.isnumeric():
      return False
    else:
      if int(i) < 0 or int(i) > 255:
        return False
  return True

for case in range(int(input())):
  s = input().split('.')
  print('NO' if len(s) != 4 or not check(s) else 'YES')