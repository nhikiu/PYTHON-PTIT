s = input()
for i in range(len(s) - 3, 0, -3):
  s = s[:i] + ',' + s[i:]
print(s)

# s = ' '.join(input()).split()
# cnt = 0
# for i in range(len(s) - 1, 0, -1):
#   cnt += 1
#   if not cnt % 3:
#     s.insert(i, ',')
# print(''.join(s))