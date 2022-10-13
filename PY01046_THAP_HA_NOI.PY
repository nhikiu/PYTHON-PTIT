def hanoi(n, p1 = 'A', p2 = 'B', p3 = 'C'):
  if n == 1:
    print(p1 + ' -> ' + p3)
    return
  hanoi(n - 1, p1, p3, p2)
  hanoi(1, p1, p2, p3)
  hanoi(n - 1, p2, p1, p3)
hanoi(int(input()))