def solve(n):
  if n <= 2: return 0
  if n <= 4: return 2.5
  if n <= 6: return 3.0
  if n <= 9: return 3.5
  if n <= 12: return 4.0
  if n <= 15: return 4.5
  if n <= 19: return 5.0
  if n <= 22: return 5.5
  if n <= 26: return 6.0
  if n <= 29: return 6.5
  if n <= 32: return 7.0
  if n <= 34: return 7.5
  if n <= 36: return 8.0
  if n <= 38: return 8.5
  if n <= 40: return 9.0

for case in range(int(input())):
  point = []
  while len(point) < 4:
    point = [float(i) for i in input().split()]
  p1, p2, p3, p4 = solve(point[0]), solve(point[1]), point[2], point[3]
  overall = (p1 + p2 + p3 + p4) / 4
  m = overall - int(overall)
  if m < 0.25: overall = int(overall)
  elif m >= 0.25 and m < 0.75: overall = int(overall) + 0.5
  elif m >= 0.75: overall = int(overall) + 1
  print('{:.1f}'.format(overall))