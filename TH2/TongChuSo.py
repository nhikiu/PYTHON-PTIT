def solve(s):
  res = 0
  for i in s:
    res += ord(i) - ord('0')
  return str(res)

s = input()
cnt = 0
while len(s) > 1:
  s = solve(s)
  cnt += 1
print(cnt)