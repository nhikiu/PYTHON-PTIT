for case in range(int(input())):
  n, m = input().split()
  n, m = int(n), int(m)
  list = input().split()
  print(*(list[m:] + list[:m]))