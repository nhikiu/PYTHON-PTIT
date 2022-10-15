n = int(input())
l = [int(i) for i in input().split()]
l.sort()
l += [l[-1] + 2]
for i in range(1, len(l)):
  if l[i] - l[i - 1] != 1:
    print(l[i - 1] + 1)
    break