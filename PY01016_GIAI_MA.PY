for case in range(int(input())):
  str = input()
  for i in range(0, len(str), 2):
    for j in range(int(str[i + 1])):
      print(str[i], end = "")
  print("")