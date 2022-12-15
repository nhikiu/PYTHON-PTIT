s1 = set(input().lower().split())
s2 = set(input().lower().split())
print(*sorted(s1.union(s2)))
print(*sorted(s1.intersection(s2)))