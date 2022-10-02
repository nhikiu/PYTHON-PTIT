def solve(n):
  sum = 0
  if n % 2:
    for i in range(1, n + 1):
      if i % 2:
        sum += 1/i
  else:
    for i in range(1, n + 1):
      if not i % 2:
        sum += 1/i
  return sum

for case in range(int(input())):
  print("{:.6f}".format((solve(int(input())))))