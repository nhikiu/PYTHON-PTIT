def solve(s):
  if not len(s) % 2 or s[0] == s[1]:
    return 'NO'
  for i in range(2, len(s), 2):
    if s[i] != s[i - 2] or s[i] != s[len(s) - 1]:
      return 'NO'
  return 'YES'

for case in range(int(input())):
  print(solve(input()))