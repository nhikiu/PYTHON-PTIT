s = input().lower()
print('yes' if s[len(s) - 3 : len(s)] == '.py' else 'no')