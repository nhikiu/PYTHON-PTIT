s = input()
n = len(s)
if n % 2 == 1: n -= 1
res = []
for i in range(0, n, 2):
  if s[i:i+2] not in res:
    res += [s[i:i+2]]
print(*sorted(res))