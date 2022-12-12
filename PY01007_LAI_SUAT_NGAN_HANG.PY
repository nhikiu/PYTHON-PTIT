from math import ceil, log

for case in range(int(input())):
  n, x, m = [float(i) for i in input().split()]
  print(ceil(log(m/n)/log(1 + x/100)))
# c2:
# for case in range(int(input())):
#   n, r, m = [float(i) for i in input().split()]
#   cnt = 0
#   while True:
#     if n >= m: break
#     cnt += 1
#     n = n * (1 + r * 0.01)
#   print(cnt)