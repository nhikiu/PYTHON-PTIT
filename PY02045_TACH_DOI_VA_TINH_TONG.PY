s = input()
while len(s) > 1:
  n = int(s[:len(s)//2]) + int(s[len(s)//2:])
  s = str(n)
  print(s)