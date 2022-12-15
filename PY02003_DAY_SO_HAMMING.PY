list = []
MAX = 10 ** 18
i = 1
while i <= MAX:
  j = 1
  while j <= MAX:
    z = 1
    while z <= MAX:
      list += [i * j * z]
      z *= 5
    j *= 3
  i *= 2

def binarySearch(n, l, r):
  if l > r: return 'Not in sequence'
  mid = (l + r) // 2
  if list[mid] == n: return mid + 1
  if list[mid] > n: return binarySearch(n, l, mid - 1)
  return binarySearch(n, mid + 1, r)

list = sorted(list)
for case in range(int(input())):
  n = int(input())
  print(binarySearch(n, 0, len(list)))