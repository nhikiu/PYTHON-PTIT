n = int(input())
a = []
while len(a) < n:
  a += [int(i) for i in input().split()]
m = max(a)
check = False
for i in range(1, m):
  if i not in a:
    print(i)
    check = True
if not check: print('Excellent!')