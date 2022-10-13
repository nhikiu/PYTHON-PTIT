res = []
n = int(input())
for i in range(n):
  str = input()
  if str not in res:
    res += [str]
print(len(res))