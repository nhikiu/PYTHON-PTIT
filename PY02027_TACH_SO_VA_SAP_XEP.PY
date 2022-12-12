import re

numbers = []
for case in range(int(input())):
  numbers += [int(i) for i in re.findall('\\d+', input())]
print(*sorted(numbers), sep = '\n')