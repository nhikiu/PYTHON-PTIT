for case in range(int(input())):
  n, m = input().split()
  inp = input().split()
  if len(inp) == 1:
    x1 = inp[0]
    x2 = input()
  else: x1, x2 = inp
  s1 = int(x1.replace(m ,n)) + int(x2.replace(m, n))
  s2 = int(x1.replace(n, m)) + int(x2.replace(n, m))
  print(f"{s1} {s2}" if s1 < s2 else f"{s2} {s1}")