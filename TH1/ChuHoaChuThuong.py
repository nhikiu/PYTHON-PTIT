cnt, s = 0, input()
for i in s:
  if str(i).isupper():
    cnt += 1
print(s.upper() if cnt > len(s) - cnt else s.lower())