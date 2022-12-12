for case in range(int(input())):
  s1, s2 = input(), input()
  print(f"Test {case + 1}: ", 'YES' if sorted(s1) == sorted(s2) else 'NO', sep = '')