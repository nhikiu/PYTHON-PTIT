for case in range(int(input())):
  s1 = ' '.join(input()).split()
  s2 = ' '.join(input()).split()
  s1.sort()
  s2.sort()
  print(f"Test {case + 1}: ", end = '')
  print('YES' if s1 == s2 else 'NO')