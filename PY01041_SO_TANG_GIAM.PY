def solve(s):
  for i in range(1, len(s)):
    if s[i - 1] <= s[i]:
      return False
  return True

for case in range(int(input())):
  n = input()
  for i in range(1, len(n)):
    if n[i] <= n[i - 1]:
      cnt = i
      break
  print('YES' if len(n) >= 3 and solve(n[cnt:]) else 'NO')