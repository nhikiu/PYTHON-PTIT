def check(s):
  if len(s) % 2 or s != s[::-1]:
    return False
  for i in s:
    if int(i) % 2:
      return False
  return True

for case in range(int(input())):
  n = int(input())
  for i in range(22, n, 2):
    if check(str(i)):
      print(i, end = ' ')
  print()