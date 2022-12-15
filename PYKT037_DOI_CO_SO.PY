ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for case in range(int(input())):
  n, b = [int(i) for i in input().split()]
  res = ''
  while n > 0:
    res += ALPHABET[n % b]
    n = n // b
  print(res[::-1])