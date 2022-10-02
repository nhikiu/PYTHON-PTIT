str = input()
countUpper, countLower = 0, 0
for i in str:
  if i.isupper():
    countUpper += 1
  elif i.islower():
    countLower += 1

if countLower >= countUpper:
  print(str.lower())
else:
  print(str.upper())