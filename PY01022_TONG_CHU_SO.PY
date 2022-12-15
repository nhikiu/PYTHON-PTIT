n, cnt = input(), 0
while len(n) > 1:
  cnt += 1
  n = str(sum((ord(i) - ord('0')) for i in n))
print(cnt)