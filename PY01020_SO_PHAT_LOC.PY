for case in range(int(input())):
  num = input()
  if num[len(num)-2:len(num)] == '86':
    print('YES')
  else:
    print('NO')