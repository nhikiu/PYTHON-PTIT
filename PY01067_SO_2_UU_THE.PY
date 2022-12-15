def check(n):
  a = n.count('0')
  b = n.count('1')
  c = n.count('2')
  return c > (len(n) // 2) and int(n) > 0

def backtrack(i, s, n, list):
  if i > n: return
  if check(s): list += [s]
  if i < n:
    backtrack(i + 1, s + '0', n, list)
    backtrack(i + 1, s + '1', n, list)
    backtrack(i + 1, s + '2', n, list)

list = []
backtrack(0, '', 9, list)
new_list = set([int(i) for i in list])
new_list = sorted(new_list)
for case in range(int(input())):
  for i in range(0, int(input())):
    print(new_list[i], end = ' ')
  print()