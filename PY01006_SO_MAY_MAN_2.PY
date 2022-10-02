test = int(input())
for case in range(test):
  list = input()
  if list.count('4') + list.count('7') == len(list) or list.count('4') + list.count('7') == len(list):
    print("YES")
  else:
    print("NO")