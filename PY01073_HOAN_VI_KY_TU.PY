import itertools

s = input()
for i in itertools.permutations(s):
  print(''.join(i))