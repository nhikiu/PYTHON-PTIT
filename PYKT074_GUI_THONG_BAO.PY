for case in range(int(input())):
  s = input()
  if len(s) <= 100: print(s)
  else:
    s = s[0:100]
    res = -1
    for i in range(len(s) - 1, 0, -1):
      if s[i] == ' ':
        res = i
        break
    print(s[0:res])