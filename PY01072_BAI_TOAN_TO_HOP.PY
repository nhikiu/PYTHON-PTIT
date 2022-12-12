n, k = [int(i) for i in input().split()]
list = sorted(list({int(i) for i in input().split()}))
n = len(list)

def solve(i, l):
  global n, k
  if len(l) == k:
    print(*l)
    return
  for j in range(i, n):
    solve(j + 1, l + [list[j]])

solve(0, [])