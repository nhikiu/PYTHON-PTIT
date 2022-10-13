def solve(s1):
  s2 = s1[::-1]
  for i in range(1, len(s1)):
    if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
      return False
  return True

for case in range(int(input())):
  s = input()
  print('YES' if solve(s) else 'NO')