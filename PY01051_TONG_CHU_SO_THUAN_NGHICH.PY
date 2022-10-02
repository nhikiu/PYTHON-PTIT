def check(s):
  s = str(sum(int(i) for i in s))
  return 'YES' if s == s[::-1] and len(s) > 1 else 'NO'

for case in range(int(input())):
  print(check(input()))