n = input()
s = [int(i) for i in input().split()]
i = 1
while i < len(s):
  if not (s[i - 1] + s[i]) % 2:
    del s[i]
    del s[i - 1]
    if i > 1:
      i -= 1
  else:
    i += 1
print(len(s))