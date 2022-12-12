for case in range(int(input())):
  s = input() + '/'
  cnt = 1
  res = ''
  for i in range(0, len(s) - 1):
    if s[i] != s[i + 1]:
      res += str(cnt) + s[i]
      cnt = 1
    else: cnt += 1
  print(res)