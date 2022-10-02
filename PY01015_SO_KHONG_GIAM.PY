def soKhongGiam(n):
  for i in range(0, len(n) - 1):
    if n[i] > n[i+1]:
      return False
  return True

for case in range(int(input())):
  num = input()
  print("YES" if soKhongGiam(num) else "NO")