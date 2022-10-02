from math import ceil, log


for case in range(int(input())):
  n, x, m = [float(i) for i in input().split()]
  print(ceil(log(m/n)/log(1 + x/100)))