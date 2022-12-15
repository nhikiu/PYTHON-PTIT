list = []
for case in range(int(input())):
  s = input()
  if s.strip() != '':
    list += [s]
  else:
    print(f"{list[0]}: {len(list) - 1}")
    list = []
if len(list) > 0:
  print(f"{list[0]}: {len(list) - 1}")