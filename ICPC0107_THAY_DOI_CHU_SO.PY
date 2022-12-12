for case in range(int(input())):
  a, b = input().split()
  inp = input().split()
  if len(inp) == 1:
    s1 = inp[0]
    s2 = input()
  else:
    s1, s2 = inp
  res1 = int(s1.replace(a, b)) + int(s2.replace(a, b))
  res2 = int(s1.replace(b, a)) + int(s2.replace(b, a))
  print(min(res1, res2), max(res1, res2))