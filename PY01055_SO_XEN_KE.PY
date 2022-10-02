def solve(s):
  if not len(s) % 2 or s[0] == s[1]:
    return False
  for i in range(2, len(s), 2):
    if s[i] != s[i - 2] or s[i] != s[len(s) - 1]:
      return False
  return True

for case in range(int(input())):
  print('YES' if solve(input()) else 'NO')