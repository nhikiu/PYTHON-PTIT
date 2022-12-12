n = input()
res = 0
for i in n:
  if i == '5' or i == '3':
    res += 1
print('YES' if res == 3 or res == 5 else 'NO')