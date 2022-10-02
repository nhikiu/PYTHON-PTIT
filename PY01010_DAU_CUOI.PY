for case in range(int(input())):
  str = input()
  if str[0:2] == str[len(str) - 2 : len(str)]:
    print('YES')
  else:
    print('NO')