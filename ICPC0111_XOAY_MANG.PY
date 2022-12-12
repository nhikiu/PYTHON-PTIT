for case in range(int(input())):
  n, m = [int(i) for i in input().split()]
  list = input().split()
  print(*(list[m:] + list[:m]))