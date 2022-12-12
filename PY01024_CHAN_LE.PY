def check(s):
  for i in range(1, len(s)):
    if abs(ord(s[i]) - ord(s[i - 1])) != 2: return False
  return True

for case in range(int(input())):
  s = ' '.join(input()).split()
  print('YES' if not sum(int(i) for i in s) % 10 and check(s) else 'NO')