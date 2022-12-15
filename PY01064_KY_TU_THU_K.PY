for case in range(int(input())):
  n, k = [int(i) for i in input().split()]
  res = ''
  for i in range(n):
    res = res + chr(ord('A') + i) + res
  print(res[k - 1])