def solve(n):
  for i in range(2, len(n)):
    if n[i] != n[i - 2]:
      return False
  return True;

for case in range(int(input())):
  print("YES" if solve(input()) else "NO")