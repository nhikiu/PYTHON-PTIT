def check(n):
  tmp = ' '.join('02468').split()
  for i in ' '.join(n).split():
    if i not in tmp:
      return False
  return True

for case in range(int(input())):
  n = int(input())
  for i in range(22, n, 22):
    if i == int(str(i)[::-1]) and check(str(i)) and not len(str(i)) % 2:
      print(i, end = ' ')
  print()