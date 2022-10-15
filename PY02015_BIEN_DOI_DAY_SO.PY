def check(list):
  for i in range(1, len(list)):
    if list[i] != list[i - 1]:
      return False
  return True

while True:
  list = [int(i) for i in input().split()]
  if list == [0] * 4:
    break
  cnt = 0
  while True:
    if check(list):
      break
    cnt += 1
    new_list = list[:]
    for i in range(0, 3):
      new_list[i] = abs(list[i] - list[i + 1])
    new_list[3] = abs(list[3] - list[0])
    list = new_list[:]
  print(cnt)