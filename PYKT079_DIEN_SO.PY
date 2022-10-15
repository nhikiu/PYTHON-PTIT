for case in range(int(input())):
  n = int(input())
  list = [int(i) for i in input().split()]
  tmp = []
  for i in list:
    if i not in tmp:
      tmp += [i]
  print(max(tmp) - min(tmp) + 1 - len(tmp))