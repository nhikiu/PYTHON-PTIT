for case in range(int(input())):
  n, m = [int(i) for i in input().split()]
  list = [int(i) for i in input().split()]
  max_value = max(list)
  list.insert(list.index(max_value), m)
  for i in list:
    if i < 0: print(i, end = ' ')
  for i in list:
    if i >= 0: print(i, end = ' ')
  print()