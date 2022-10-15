for case in range(int(input())):
  list = [0] * 1001
  for i in range(int(input())):
    list[int(input())] += 1
  print(list.index(max(list)))