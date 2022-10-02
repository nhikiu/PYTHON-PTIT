import math

def check(org_str):
  str = list(org_str)
  str.reverse()
  new_str = ''.join(str)
  for i in range(1, len(org_str)):
    if math.fabs(ord(org_str[i]) - ord(org_str[i-1])) != math.fabs(ord(new_str[i]) - ord(new_str[i-1])):
      return False
  return True

for case in range(int(input())):
  org_str = input()
  if check(org_str):
    print('YES')
  else:
    print('NO')