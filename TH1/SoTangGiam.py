def check1(s):
  for i in range(1, len(s)):
    if s[i] <= s[i-1]:
      return False
  return True

def check2(s):
  for i in range(len(s)):
    if check1(s[0:i + 1:1]) and check1(s[i::][::-1]):
      return True
  return False

for case in range(int(input())):
  n = input()
  print('YES' if check2(n) and len(n) >= 3 else 'NO')