for case in range(int(input())):
  n = int(input())
  arr = [int(i) for i in input().split()]
  arr.sort()
  check = 0
  for i in arr:
    cnt = arr.count(i)
    if cnt > n/2:
      check = 1
      print(i)
      break
  if not check: print('NO')