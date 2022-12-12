n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
A, B = set(a), set(b)
print('YES' if A == B else 'NO')