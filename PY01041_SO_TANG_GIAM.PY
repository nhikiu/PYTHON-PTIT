def check(s):
  for i in range(1, len(s)):
    if s[i] <= s[i-1]:
      return False
  return True

def solve(s):
  for i in range(len(s)):
    if check(s[0:i + 1:1]) and check(s[i::][::-1]):
      return True
  return False

for case in range(int(input())):
  n = input()
  print('YES' if solve(n) and len(n) >= 3 else 'NO')

# def solve(n):
#   if len(n) < 3:
#     return False
#   i = 1
#   while i < len(n) and n[i - 1] < n[i]:
#     i += 1
#   while i < len(n) and n[i - 1] > n[i]:
#     i += 1
#   return True if i == len(n) else False

# for case in range(int(input())):
#   print('YES' if solve(input()) else 'NO')