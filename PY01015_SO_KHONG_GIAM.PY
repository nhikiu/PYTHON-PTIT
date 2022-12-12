def check(n):
  for i in range(1, len(n)):
    if n[i - 1] > n[i]: return False
  return True

for case in range(int(input())):
  print('YES' if check(input()) else 'NO')