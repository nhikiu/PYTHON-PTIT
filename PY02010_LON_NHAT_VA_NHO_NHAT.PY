def check(list):
  for i in range(1, len(list)):
    if list[i] != list[i - 1]:
      return False
  return True

while True:
  n = int(input())
  if n == 0:
    break
  list = []
  for i in range(n):
    list += [int(input())]
  print('BANG NHAU' if check(list) else f"{min(list)} {max(list)}")