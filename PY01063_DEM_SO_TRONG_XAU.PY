for case in range(int(input())):
  s, n = input(), input()
  cnt, ind = 0, s.find(n)
  while ind != -1:
    cnt += 1
    ind = s.find(n, ind + len(n))
  print(cnt)