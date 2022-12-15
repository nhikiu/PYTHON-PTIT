lines = []
for line in range(int(input())):
  lines += [len(input().split())]
res = []
i = 0
while i < len(lines):
  if lines[i] == 7:
    i += 4
    res += [2]
  elif lines[i] == 6:
    i += 2
    res += [1]
    while i < len(lines) and lines[i] == 6:
      i += 2
print(len(res))
print(*res, sep='\n')