n = int(input())
list = input().split()
min, max = float(list[0]), float(list[0])
for i in list:
  if float(i) < min: min = float(i)
  if float(i) > max: max = float(i)

for i in list:
  if float(i) == min or float(i) == max:
    list.remove(i)

print(round(sum(float(i) for i in list) / len(list), 2))
